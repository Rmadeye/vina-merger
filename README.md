# vina-merger
AutoDockVina input protein - output docking files merger

For automatable version check CLI branch

## Installation
1. Clone this repository
```
$ git clone https://github.com/Rmadeye/vina-merger.git
```
2. As all required packages are present in **requirements.txt** file, using virtual environment is strongly recommended.
If virtualenv is not installed:
```
$ pip3 install virtualenv
```
Create virtual environment and install required packages
```
$ cd venvs_location
$ virtualenv vina-merger
$ source vina-merger/bin/activate
$ pip install -r requirements.txt
```
## Usage
```
$ python3 merge-it.py
```
Once the window is open, following steps must be followed:
1. Choose pdb structure of your protein **before** docking
2. Choose pdb/pdbqt file of your docked file.
3. Click **run**, results are found in /out directory

## Important

1. Remember to have **only one model** in the ligand pdbqt/pdb file (probably the one with the lowest energy). Otherwise all poses of the ligands and flexible chains will be printed in output pdb.
2. The script does not add/remove hydrogen atoms. Check output protonation states.
3. If you are not sure if the script worked, perform RMSD analysis (using biopandas, biopython, PyMol etc).
