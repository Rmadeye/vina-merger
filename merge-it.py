import argparse, time
from src.system_preparation import PDBQTprep
from src.conversion import Converter



class AppRun:

    start = time.time()

    inputdata = argparse.ArgumentParser(description="Process docking files")

    inputdata.add_argument('-ir', '--rigid-pdb', nargs='*',
                           help="Input rigid pdb file", required=True, )
    inputdata.add_argument('-if', '--flex-pdb', nargs='*',
                           help="Input flexible pdb file", required=True)

    args = inputdata.parse_args()

    convert = PDBQTprep(args.rigid_pdb[0], args.flex_pdb[0]).files_preparation()
    end = time.time()

    print("The operation took {}".format(end - start))
