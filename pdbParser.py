from Bio.PDB import *


def getStructure(name, filename):
    parser = PDBParser()
    structure = parser.get_structure(name, filename)    
    for atom in structure.get_atoms():
        print(atom)

getStructure("glukoza", "glucose.pdb")

