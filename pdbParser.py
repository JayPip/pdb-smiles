from Bio.PDB import *
import autode as ade

def getStructureFromPDB(name, filename):
    parser = PDBParser()
    structure = parser.get_structure(name, filename)    
    for atom in structure.get_atoms():
        print(atom)

def getStructureFromSmiles(filename):
    f = open(filename, "r")
    smiles = f.readline()
    f.close()
    SParser = ade.Parser()
    SParser.parse(smiles)

getStructureFromSmiles("glucose.smi")
getStructureFromPDB("glukoza", "glucose.pdb")

