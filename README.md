# vina-merger
AutoDockVina input protein - output docking files merger  - command line version

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
However, *virtualenv* may have problem with plip package. Unless you need it, you may use virtualenv. Otherwise i
strongly recommend *conda* environment. Create virtual environment and install required packages
```
$ cd venvs_location
$ virtualenv vina-merger
$ source vina-merger/bin/activate
$ pip install -r requirements.txt
```
## Usage
```
$ ./merge-it.py -ir protein.pdb -if ligand.pdb(qt) -p (optional, for PLIP interaction autoanalysis) -m (if multiple models in pdbqt, default 1)
```

## Important

1. Remember to have your **favourite model** in the ligand pdbqt/pdb file (probably the one with the lowest energy).
2. Hydrogen atoms are removed. PLIP add them and can be found inside working directory. Check output protonation states.
3. If you are not sure if the script worked, perform RMSD analysis (using biopandas, biopython, PyMol etc).
