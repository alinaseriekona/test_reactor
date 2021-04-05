"""
Constant-pressure, adiabatic kinetics simulation.

Requires: cantera >= 2.5.0, matplotlib >= 2.0
"""

import sys
import cantera as ct
import csv


# Read input data file
InputDict = {}
with open('input.txt', 'r') as fi:
    for line in fi:
        splitline = line.split()
        InputDict[str(splitline[0])] = float(splitline[1]) 

# Set the initial condidtions
composition = 'CH4:'+str(InputDict['CH4'])+',O2:'+str(InputDict['O2'])+',N2:'+str(InputDict['N2'])
dt_max = InputDict['deltaT']
t_end = InputDict['t_final']
n_it = int(t_end/dt_max)
T0 = InputDict['temperature']
P0 = InputDict['pressure']

# Chemical kinetic mechanism specification
gas = ct.Solution('gri30.yaml')
gas.TPX = T0, P0*ct.one_atm, composition


r = ct.IdealGasConstPressureReactor(gas)

sim = ct.ReactorNet([r])
sim.verbose = True

# limit advance when temperature difference is exceeded
#delta_T_max = 20.
#r.set_advance_limit('temperature', delta_T_max)

states = ct.SolutionArray(gas, extra=['t'])


# Print the out put on the screen
#print('{:5s}, {:5s}, {:5s}, {:9s}'.format('t [s]', 'T [K]', 'P [Pa]', 'u [J/kg]'))


while sim.time < t_end:
    sim.advance(sim.time + dt_max)
    states.append(r.thermo.state, t=sim.time*1e3)

    # Print the output on the screen
    # print('{:10.3e}, {:10.3f}, {:10.3f}, {:14.6f}'.format(sim.time, r.T, r.thermo.P, r.thermo.u))




# write output CSV file for importing into Excel

csv_file = 'output.csv'
with open(csv_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['t (s)', 'T (K)', 'Pa (Pa)'] +gas.species_names)
    for i in range(n_it):
        writer.writerow([states.t[i]/1000, states.T[i], states.P[i]]+[j for j in states.X[i]])


# Plot the results if matplotlib is installed.
# See http://matplotlib.org/ to get it.
if '--plot' in sys.argv[1:]:
    import matplotlib.pyplot as plt
    plt.clf()
    plt.subplot(2, 2, 1)
    plt.plot(states.t, states.T)
    plt.xlabel('Time (ms)')
    plt.ylabel('Temperature (K)')
    plt.subplot(2, 2, 2)
    plt.plot(states.t, states.X[:, gas.species_index('CH4')])
    plt.xlabel('Time (ms)')
    plt.ylabel('CH4 Mole Fraction')
    plt.subplot(2, 2, 3)
    plt.plot(states.t, states.X[:, gas.species_index('CO2')])
    plt.xlabel('Time (ms)')
    plt.ylabel('CO2 Mole Fraction')
    plt.subplot(2, 2, 4)
    plt.plot(states.t, states.X[:, gas.species_index('H2')])
    plt.xlabel('Time (ms)')
    plt.ylabel('H2 Mole Fraction')
    plt.tight_layout()
    plt.show()
else:
    print("To view a plot of these results, run this script with the option --plot")
