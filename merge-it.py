import argparse
import time

from src.conversion import Converter

start = time.time()

inputdata = argparse.ArgumentParser(description="Process docking files")

inputdata.add_argument('-ir', '--rigid-pdb', nargs='*',
                       help="Input rigid pdb file", required=True, )
inputdata.add_argument('-if', '--flex-pdb', nargs='*',
                       help="Input flexible pdb file", required=True)

args = inputdata.parse_args()

convert = Converter(args.rigid_pdb[0], args.flex_pdb[0]).convert()
end = time.time()

print("The operation took {}".format(end - start))
