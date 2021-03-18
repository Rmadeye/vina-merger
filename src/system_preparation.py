import os

from biopandas.pdb import PandasPdb

from src.conversion import Converter


class PDBQTprep:
    def __init__(self, protein_file: str, flex_file: str, model: int, plip: bool):
        self.prot = protein_file
        self.flex = flex_file
        self.protname = os.path.basename(self.prot)
        self.flexname = os.path.basename(self.flex)
        self.model = int(model)
        self.plip = plip

    def files_preparation(self):
        def clean_pdbqt(file, model):
            output_file = file.split('.')[0]
            switch = 0
            with open(f'{file}', 'r') as idf:
                with open(f'{output_file}_model_{model}.pdbqt', 'w') as odf:
                    for line in idf:
                        if (line.split()[0] == 'MODEL') and (line.split()[1] == f"{model}"):
                            switch += 1
                        if switch == 1:
                            odf.write(line)
                        if (line.split()[0] == 'MODEL') and (line.split()[1] == f"{model + 1}"):
                            break
            print(f"clean_pdb path: {output_file}_model_{model}.pdbqt")
            return f"{output_file}_model_{model}.pdbqt"

        def save_cleaned(file):
            output_file = file.split('.')[0]
            df = PandasPdb().read_pdb(file)
            print(df)
            df.df['ATOM']['segment_id'] = df.df['ATOM']['segment_id'].iloc[0:0]
            df.df['ATOM']['segment_id'] = df.df['ATOM']['segment_id'].fillna('')
            df.df['ATOM']['blank_4'] = df.df['ATOM']['blank_4'].iloc[0:0]
            df.df['ATOM']['blank_4'] = df.df['ATOM']['blank_4'].fillna('')
            df.df['ATOM'] = df.df['ATOM'][df.df['ATOM']['element_symbol'] != 'H']
            df.df['ATOM']['element_symbol'].replace(to_replace='A', value='C', inplace=True)
            df.df['ATOM'].drop(['charge'], axis=1)
            df.df['ATOM'].drop(['line_idx'], axis=1)
            return df.to_pdb(path=f'{output_file}-prep.pdb',
                             records=['ATOM', 'HETATM'],
                             gz=False,
                             append_newline=True)

        def prepare_protein():
            prot_df = PandasPdb().read_pdb(self.prot)
            prot_df.df['ATOM'] = prot_df.df['ATOM'][prot_df.df['ATOM']['element_symbol'] != 'H']  # deprotonate
            prot_df.df['ATOM']['residue_name'].replace(to_replace='CYX', value='CYS', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='HIE', value='HIS', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='HID', value='HIS', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='HIP', value='HIS', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='ASX', value='ASN', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='GLX', value='GLN', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='GLH', value='GLN', inplace=True)
            prot_df.df['ATOM']['residue_name'].replace(to_replace='LYN', value='LYS', inplace=True)

            return prot_df.to_pdb(path=os.getcwd() + '/{}-dehyd.pdb'.format(self.protname.split('.')[0]),
                                  records=['ATOM', 'HETATM'],
                                  gz=False,
                                  append_newline=True)

        if self.flex.endswith('.pdbqt'):
            return prepare_protein(), \
                   save_cleaned(clean_pdbqt(file=self.flex, model=self.model)), \
                   Converter(os.getcwd() + f'/{self.protname.split(".")[0]}-dehyd.pdb',
                             os.getcwd() + f'/{self.flexname.split(".")[0]}_model_{self.model}-prep.pdb',
                             self.plip).convert()
        if self.flex.endswith('pdb'):
            prepare_protein()
            save_cleaned(self.flex)
            Converter(os.getcwd() + '/{}-dehyd.pdb'.format(self.protname.split('.')[0]),
                      os.getcwd() + '/{}-prep.pdb'.format(self.flexname.split('.')[0]), self.plip).convert()
        else:
            print("Incorrect file extension. Only pdb/pdbqt accepted")
