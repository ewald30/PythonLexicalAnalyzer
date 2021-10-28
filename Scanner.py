import re

class Scanner:

    def __init__(self, symbolTable, pif):
        self._symbolTable = symbolTable
        self._pif = []


    def execute(self, inputFile, pifFileName, symbolTableFileName):
        tokens = self.tokenize(inputFile)
        self.scan(tokens, inputFile, pifFileName, symbolTableFileName)

    def tokenize(self, inputFile):
        lineNumber = 1
        tokens = []
        file = open(inputFile, "r")
        lines = file.readlines()

        for line in lines:
            temp = re.split("((?<=[{}:;,()\s\t\n=%<>]|\\+|\\*)|(?=[{}:;,()\s\t\n=%<>]|\\+|\\*))", line)
            temp = list(filter(('').__ne__, temp))      # removes the empty characters ''
            temp = list(filter(('\n').__ne__, temp))    # removes the newline character
            for item in temp:
                tokens.append([item, lineNumber])
            lineNumber += 1
        file.close()
        return tokens


    def scan(self, tokens, inputFileName, pifFileName, symbolTableFileName):
        status = ""
        for token in tokens:
            if self.checkReservedWord(token[0]) or self.checkOperator(token[0]) or self.checkSeparator(token[0]):
                self._pif.append([token[0], -1])
            elif self.checkIdentifier(token[0]) or self.checkConstant(token[0]):
                symtableIndex = self._symbolTable.insert(token[0],0)
                self._pif.append([token[0], symtableIndex])
            else:
                status += "\n          Lexical error! Line: " + str(token[1]) + " Token: " + str(token[0]) + "\n\n"

        if status == "":
            status += "\n          Lexically correct!\n\n"

        self.writePIF(inputFileName, pifFileName, status)
        self.writeSymbolTable(inputFileName, symbolTableFileName, status)


    def writeSymbolTable(self, inputFileName, symbolTableFileName, status):
        symtableFile = open(symbolTableFileName, 'w')
        inputFile = open(inputFileName, 'r')
        symtableFile.write("/---------------- INPUT ----------------/\n\n")
        symtableFile.write(inputFile.read())
        symtableFile.write("\n/---------------------------------------/\n\n\n\n")
        symtableFile.write("\n/---------------- STATUS ----------------/\n")
        symtableFile.write(status)
        symtableFile.write("/---------------------------------------/\n\n\n\n\n\n\n")
        symtableFile.write(str(self._symbolTable))
        symtableFile.close()


    def writePIF(self, inputFileName, pifFileName, status):
        pifFile = open(pifFileName, 'w')
        inputFile = open(inputFileName, 'r')
        pifFile.write("/---------------- INPUT ----------------/\n\n")
        pifFile.write(inputFile.read())
        pifFile.write("\n/---------------------------------------/\n\n\n\n")
        pifFile.write("\n/---------------- STATUS ----------------/\n")
        pifFile.write(status)
        pifFile.write("/---------------------------------------/\n\n\n\n\n\n\n")
        pifFile.write("/----------------  PIF  ----------------/\n\n")
        for pifItem in self._pif:
            pifFile.write(str(pifItem[0]) + " : " + str(pifItem[1]) + "\n")
        pifFile.write("/---------------------------------------/\n\n\n\n")
        pifFile.close()


    def checkReservedWord(self, token):
        if re.match("false|true|if|for|output|input|while|and|or|int|char|const|else|bool|string",token):
            return True
        return False

    def checkOperator(self, token):
        if re.match("<|>|<=|>=|=|<->|\\+|-|//|\\*|%|<>", token):
            return True
        return False

    def checkSeparator(self, token):
        if re.match("[{}:;,()\s\t\n]", token):
            return True
        return False

    def checkIdentifier(self, token):
        if re.match("^[A-Za-z][a-zA-Z0-9_]*$", token):
            return True
        return False

    def checkConstant(self, token):
        # strings
        if re.match("^\"[a-zA-Z0-9_]*\"$", token):
            return True

        # character
        if re.match("'[A-Za-z0-9_]'", token):
            return True

        # integers
        if re.match("^[-+]?[0-9]+$", token):
            return True

        if re.match("^[a-zA-Z][\[A-Za-z0-9]*]$", token):
            return True

        return False
