


def readFile():
    pdbFile = open("sample.txt", "r")

    for line in pdbFile:
        lineContent = line.split()
        if lineContent[0] == "HETATM":
            print(lineContent)

readFile()
