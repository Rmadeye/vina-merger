from src.conversion import Converter
from tkinter import *
from tkinter import filedialog


class WindowFrame(Frame):

    def browse_protein(self):
        self.protfile = filedialog.askopenfilenames(filetypes=[("Protein file", "*.pdb")])

        self.protein_label = Label(self, text="Protein file: {}".format(self.protfile[0])
                                   ).grid(row=1, column=1)
        self.update()
        return self.protfile

    def browse_ligands(self):
        self.ligfiles = list(filedialog.askopenfilenames(filetypes=[("Ligand files", ["*.pdb", '*.pdbqt'])]))

        self.ligand_label = Label(self, text="{} ligand(s) were chosen".format(len(self.ligfiles))
                                  ).grid(row=2, column=1)
        self.update()
        return self.ligfiles

    def run(self, protein, ligands: list):
        for file in ligands:
            Converter(protein, file).convert()
        self.done_label = Label(self, text="Files converted").grid(row=3, column=1)



    def create_widgets(self):
        text = "Welcome to Protein-Ligand Merger. \n Select your PDB protein and ligand(s) files and press 'Run'." \
               "\nShould you have any questions or suggestions, write an email to rafmadaj@gmail.com"

        self.welcome_label = Label(self, text=text).grid(row=0, column=0)
        self.select_protein_button = Button(self, text="Select protein PDB",
                                            command=self.browse_protein).grid(row=1, column=0)

        self.select_ligand_button = Button(self, text="Select ligand(s) PDB",
                                           command=self.browse_ligands).grid(row=2, column=0)

        self.run_button = Button(self, text="Run", command=lambda: [self.run(self.protfile[0],
                                                                             self.ligfiles),
                                                                    ]).grid(row=3,column=0)

        self.exit_button = Button(self, text="Exit", command=quit).grid(row=4, column=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("PDB Protein-Ligand Merger")
        self.pack()
        self.create_widgets()
        self.mainloop()


if __name__ == "__main__":
    WindowFrame()
