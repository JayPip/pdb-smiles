
import molecule
import re

class Parser:
    def __init__(self, smiles = None, name = None):
        self.smiles = smiles
        self.molName = name
        self.mol = molecule.Mol(name)

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

        parts = re.split(r'(\(.+?\))',smiles)
        #numer porzadkowy 
        #wzor stechiometryczny
        #liczba wodorow
        #liczba wiazan

        for p in parts:
            tokens = re.findall('[COSNP]\d*=?|-?|#?|:?|[-=#:][COSNP]',p)
            while("" in tokens) :
                tokens.remove("")
            print('  Part "{}"'.format(p), 'have the following tokens', tokens)
            
            for token in tokens:
                element = re.search('[COSNP]',token)
                if element:
                    self.mol.addAtom(element[0])

                Connection = re.search('[COSNP]\d',token)
                if Connection:
                    self.mol.atoms[-1].numberConnection = int(Connection[0][1])
                
                atomBond = re.search('[COSNP]l?\d*[-=#:]',token)
                if atomBond:
                    self.mol.addBond(atomBond[0][len(atomBond[0])-1])
                    self.mol.atoms[-1].rightBond = molecule.Bonds.index(atomBond[0][len(atomBond[0])-1])+1
                    if len(self.mol.atoms)> 1:
                        if self.mol.atoms[-2].rightBond != 0:
                            self.mol.atoms[-1].leftBond = self.mol.atoms[-2].rightBond

                else:
                    self.mol.addBond("-")
                    #change only for atoms different from the last
                    #dont change for last in side chain
                    if p != parts[-1] and token != tokens[-1] or p[0] != "(" and tokens[-1] != token:
                        self.mol.atoms[-1].rightBond = 1
                    if self.mol.atoms[-2].rightBond != 0:
                        self.mol.atoms[-1].leftBond = self.mol.atoms[-2].rightBond
                
                sideChain = re.search('[-=#:][COSNP]', token)
                if sideChain:
                    self.mol.addBond(sideChain[0][0])
                    self.mol.atoms[-1].leftBond = molecule.Bonds.index(sideChain[0][0])+1
                    self.mol.atoms[-2].rightBond = molecule.Bonds.index(sideChain[0][0])+1
                
                
        #create bonds between atoms with number connection
        for i in range(len(self.mol.atoms)):
            for j in range(i+1,len(self.mol.atoms)):
                if self.mol.atoms[i].numberConnection ==self.mol.atoms[j].numberConnection and self.mol.atoms[i].numberConnection != 0:
                    self.mol.addBond("-")  
                    self.mol.bonds[-1].firstAtomIndex = i
                    self.mol.bonds[-1].secondAtomIndex = j
        

        
