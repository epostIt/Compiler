import fileinput

FILE_PATH = '/Users/susanpost/Desktop/Compiler/11/Average/Main.jack'
class ErrorWriting():
    
    @staticmethod
    def checkIfLineIsComment(line):
        return line.startswith('//')


    @staticmethod# function that searches for the string causing a problem and finds the line number it is on
    def printError(stringLookingFor, error):
        with fileinput.input(files=(FILE_PATH)) as f:
            for line in f:
                if stringLookingFor in line:
                    if not checkIfLineIsComment(line):
                        print("ERROR:" + error + " - Line " +
                              str(fileinput.lineno()) + ": " + line)
