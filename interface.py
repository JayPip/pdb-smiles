import smilesParser

case = -1
while case != 0:
    print("===Smiles Graphs===")
    print("1: Parse smiles")
    print("0: Exit")
    case = int(input("Choose option:"))

    if(case == 1 ):
        name = input("Molecule name: ")
        smiles = input("Smiles string:")
        parser = smilesParser.Parser(smiles, name)
        parser.parse()
        parser.molecule.displayMol()
   