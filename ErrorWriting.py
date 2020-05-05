import fileinput

FILE_PATH = '/Users/Elisabeth/Desktop/Compilers/Compiler/s2020x/Map.jack'
class ErrorWriting():
    
    @staticmethod
    def checkIfLineIsComment(line):
        return line.startswith('//')


    @staticmethod# function that searches for the string causing a problem and finds the line number it is on
    def printKnownError(expected, self, compiling, foundToken):
        with fileinput.input(files=(FILE_PATH)) as f:
            lineNumber = self.tokenizer.tokenList[0].line - 2
            count = 0
            for line in f:
                if count == lineNumber:
                    # print(FILE_PATH + ": " + line)
                    # print("Compiling: " + compiling)
                    # print("Expecting: " + expected)
                    # print("Found: " + self.getinfo())
                    f = open("ErrorFile.txt", "a")
                    f.write(FILE_PATH + "\n")
                    f.write("Line: " + line + '\n')
                    f.write("Compiling: " + compiling + '\n')
                    f.write("Expecting: " + expected + '\n')
                    f.write("Found: " + foundToken)
                    f.close()
                    break
                else:
                    count = count + 1
        
    def printUnknownError(error):
        with fileinput.input(files=(FILE_PATH)) as f:
            f = open("ErrorFile.txt", "a")
            f.write(FILE_PATH + "\n")
            f.write(error)
            f.close()


    # @staticmethod
    # def printLine(lineNumber):
        