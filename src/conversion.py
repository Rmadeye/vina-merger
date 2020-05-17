from biopandas.pdb import PandasPdb
import numpy as np, os
from datetime import datetime

class Converter:
    def __init__(self, protein_file, flex_file):
        self.protein = protein_file
        self.flex = flex_file

    def convert(self):

        time = datetime.now().strftime("%D %H:%M:%S")

        prot_df = PandasPdb().read_pdb(self.protein)
        flex_df = PandasPdb().read_pdb(self.flex)


        aalist = ['ALA', 'ARG','ASN','ASP','CYS','GLU','GLN','GLY','HIS',
                          'ILE','LEU','LYS','MET','PHE','PRO','SER',
                          'THR','TRP','TYR','VAL', 'HIE','HID','ASX','GLX']


        flex_df.df['ATOM'].loc[
            ~flex_df.df['ATOM']['residue_name'].isin(aalist), 'record_name'] = 'HETATM'

        for index, row in flex_df.df['ATOM'].iterrows():
            prot_df.df['ATOM']['x_coord'] = np.where((prot_df.df['ATOM']['residue_name'] == row['residue_name']) &
                                                       (prot_df.df['ATOM']['residue_number'] == row['residue_number']) &
                                                 (prot_df.df['ATOM']['atom_name'] == row['atom_name']),
                                                      row['x_coord'], prot_df.df['ATOM']['x_coord'])
            prot_df.df['ATOM']['y_coord'] = np.where((prot_df.df['ATOM']['residue_name'] == row['residue_name']) &
                                                       (prot_df.df['ATOM']['residue_number'] == row['residue_number']) &
                                                 (prot_df.df['ATOM']['atom_name'] == row['atom_name']),
                                                      row['y_coord'], prot_df.df['ATOM']['y_coord'])
            prot_df.df['ATOM']['z_coord'] = np.where((prot_df.df['ATOM']['residue_name'] == row['residue_name']) &
                                                       (prot_df.df['ATOM']['residue_number'] == row['residue_number']) &
                                                 (prot_df.df['ATOM']['atom_name'] == row['atom_name']),
                                                      row['z_coord'], prot_df.df['ATOM']['z_coord'])

        if len(flex_df.df['HETATM']) == 0:
            hetatms = flex_df.df['ATOM'].loc[flex_df.df['ATOM']['record_name'] == 'HETATM']
            prot_df.df['ATOM'] = prot_df.df['ATOM'].append(hetatms, ignore_index = True)
        else:
            hetatm_df = flex_df.df['HETATM']
            hetatm_df['segment_id'] = hetatm_df['segment_id'].iloc[0:0]
            hetatm_df['segment_id'] = hetatm_df['segment_id'].fillna('')
            hetatm_df['blank_4'] = hetatm_df['blank_4'].iloc[0:0]
            hetatm_df['blank_4'] = hetatm_df['blank_4'].fillna('')
            hetatm_df = hetatm_df.drop(['line_idx'], axis = 1)


            prot_df.df['ATOM'] = prot_df.df['ATOM'].append(hetatm_df, ignore_index = True)

        prot_df.df['OTHERS'] = prot_df.df['OTHERS'].iloc[0:0]

        remarks = {'record_name': 'REMARK',
            'entry': '  Created on {}, using mrfpdb by Rmadeye'.format(time)}


        prot_df.df['OTHERS'] = prot_df.df['OTHERS'].append(remarks, ignore_index = True)
        output_name = (
                os.path.basename(self.protein).split('.')[0]+'-'+(
            os.path.basename(self.flex)).split('.')[0]+'.pdb'
        )

        return prot_df.to_pdb(path='out/{}'.format(output_name),
                     records=['ATOM','OTHERS'],
                     gz=False,
                     append_newline=True)
