class Atom:
    def __init__(self, element):
        self.element = element
        self.index = -1
        self.leftBond = 0
        self.rightBond = 0
        self.numberConnection = 0

class Bond:
    def __init__(self, symbol):
        self.symbol = symbol
        self.firstAtomIndex = -1
        self.secondAtomIndex = -1

    def getBondType():
        return -1

#List of bond types
Bonds = ["-", "=", "#",":"]


class Mol:

    def __init__(self, name = None):
        self.name = name
        self.atoms = []
        self.bonds = []
        self.formula = ""
    #create new atom object and add it to list
    def addAtom(self, atomSymbol):
        atom = Atom(atomSymbol)
        atom.index = len(self.atoms)
        self.atoms.append(atom)
    
    def addBond(self,type):
        bond = Bond(type)
        self.bonds.append(bond)

    def displayMol(self):
        print("===================")
        if self.name != None:
            print("Molecule Name: ")
            print(self.name)

        print("Molecule Atoms:")
        for atm in range(len(self.atoms)):
            print(str(self.atoms[atm].index)+ ". " + self.atoms[atm].element+ " " + str(self.atoms[atm].leftBond) + " " +str(self.atoms[atm].rightBond)) 
        print("Molecule Bonds:")
        for bnd in range(len(self.bonds)):
            print(str(self.bonds[bnd].firstAtomIndex) + " " 
                + str(self.bonds[bnd].secondAtomIndex) + " "
                + self.bonds[bnd].symbol) 
        print("===================")