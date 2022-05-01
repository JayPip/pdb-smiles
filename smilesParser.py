

class Atom:
    def __init__(self, element):
        self.element = element
        self.index = -1

class Bond:
    def __init__(self, symbol):
        self.symbol = symbol
        self.firstAtomIndex = -1
        self.secondAtomIndex = -1

    def getBondType():
        return -1

#List of bond types
Bonds = ["-", "=", "#"]


class Molecule:

    def __init__(self, name = None):
        self.name = name
        self.atoms = []
        self.bonds = []

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
            print(str(self.atoms[atm].index)+ ". " + self.atoms[atm].element) 
        print("Molecule Bonds:")
        for bnd in range(len(self.bonds)):
            print(str(self.bonds[bnd].firstAtomIndex) + " " 
                + str(self.bonds[bnd].secondAtomIndex) + " "
                + self.bonds[bnd].symbol) 
        print("===================")

class Parser:
    def __init__(self, smiles = None, name = None):
        self.smiles = smiles
        self.molName = name
        self.molecule = Molecule(name)

    #get smiles
    def getSmiles(self):
        return self.smiles

    #set smiles
    def setSmiles(self, smiles):
        self.smiles = smiles

    #parse given smiles string to a molecule object
    def parse(self, smiles = None):
        if smiles == None:
            smiles = self.getSmiles()
        elif  smiles == None & self.smiles == None:
            print("No smiles string given")
            return 
        else: 
            self.setSmiles(smiles)

        #flags
        sideChain = -1
        squareBracket = -1
        isBond = -1

        for i,v in enumerate(smiles):
            #check if char is a Atom
            if v.isalpha():
                if isBond == 1:
                    lastIndex = self.molecule.atoms[-1].index
                    self.molecule.addAtom(v)
                    self.molecule.bonds[-1].firstAtomIndex = lastIndex
                    self.molecule.bonds[-1].secondAtomIndex = self.molecule.atoms[-1].index
                    isBond = 0
                else:
                    self.molecule.addAtom(v)
                
            elif v == "(":
                sideChain = 1
                continue
            elif v == "[":
                squareBracket = 1
                continue
            elif v in Bonds: 
                isBond = 1
                self.molecule.addBond(v)
