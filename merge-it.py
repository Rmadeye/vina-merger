#!/usr/bin/env python3
import argparse
import time

from src.system_preparation import PDBQTprep

start = time.time()

inputdata = argparse.ArgumentParser(description="Process docking files")

inputdata.add_argument('-ir', '--rigid-pdb', nargs='*',
                       help="Input rigid pdb file", required=True, )
inputdata.add_argument('-if', '--flex-pdb', nargs='*',
                       help="Input flexible pdb file", required=True)
inputdata.add_argument('-m', '--model', nargs='*',
                       help="Model from pdbqt file", required=False)
inputdata.add_argument('-p', '--plip', action='store_true',
                       help="Local PLIP calculations", required=False)

args = inputdata.parse_args()
convert = PDBQTprep(protein_file=args.rigid_pdb[0],
                    flex_file=args.flex_pdb[0],
                    model=args.model[0] if args.model else 1,
                    plip=args.plip).files_preparation()
end = time.time()

print("The operation took {}".format(end - start))
