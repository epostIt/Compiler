import fileinput

FILE_PATH = '/Users/susanpost/Desktop/Compiler/11/Average/Main.jack'
class ErrorWriting():
    
    @staticmethod
    def checkIfLineIsComment(line):
        return line.startswith('//')


    @staticmethod# function that searches for the string causing a problem and finds the line number it is on
    def printError(expected, recieved, lineNumber):
        f = open("ErrorFile.txt", "a")
        f.write("ERROR:" + error + " - Line " + str(fileinput.lineno()) + ": " + line + "\n")
        f.close()

    @staticmethod
    def printLine(lineNumber):
        