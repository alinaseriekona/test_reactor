# test_reactor
This project is a sample test for vendor inquiries. The code simulates an ideal constant pressure reactor at a given initial temperature, 
pressure, and mixture composition during a desired residence time. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; inputfile: input.txt, the input file is used to specify the initial conditions of the reactor.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; outputfile: output.csv, the output file is used for importing data into Excel or other applications. 


### Requirements
This code requires Python 3 and Cantera libraries. For Cantera installation, the following links are useful:
  
  Installing with Conda (highly recommended for all users):
  https://cantera.org/install/conda-install.html
  
  Installing on Windows:
  https://cantera.org/install/windows-install.html
  
  Installing on macOS:
  https://cantera.org/install/macos-install.html
  
  Installing on Ubuntu:
  https://cantera.org/install/ubuntu-install.html
  
### Running the code
1. Once Cantera is installed, activate the environment created for Cantera. 
E.g., conda activate spam, in case you are using Conda.

2. Download the code (reactor_CH4.py) in the desired directory.

3. Using the following command in the command line, the code can be executed:
python3 reactor_CH4.py

### Code outputs
1. The code plots the temperature, CH4, CO2, and H2 mole fraction profiles if the code is executed with the argument --plot (python3 reactor_CH4.py --plot).

2. Besides, a detailed CSV file is saved in the directory for importing the solution into Excel or 
equivalent data processing software. 
