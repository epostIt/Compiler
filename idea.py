import fileinput
import re

# FILE_PATH = '/Users/Elisabeth/Desktop/Compilers/Compiler/11/Average/Main.jack'
delimiters = r'([\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|(?:"[^"]*")| *)'
comment=r'(?:(\/\*(.|\n)*?\*\/)|(//.*))'
array = ['class', 'Main', '{']
#what if I read in one line of tokens at a time, tokenize them, attach them to a line number, then increment line and count

class TokenObject:
    tokenObjectList = []

    def __init__(self, token, line):
        self.line = line
        self.value = token

    def breakListIntoTokens(tokenList, line):
        for token in tokenList:
            ob = TokenObject(token, line)
            TokenObject.tokenObjectList.append(ob)
            # print(ob.line)
            # print(ob.value)
    def readOneLineAtATime():
        totalList = []
        with fileinput.input(files=(FILE_PATH)) as f:
            count = 0
            for line in f:  #read one line of the file in at a toke
                inp = " ".join(re.sub(comment,"",line).split())
                tokenList=[token for token in re.split(delimiters,inp) if token not in ('', ' ')] #tokenize that one line
                count = count + 1
                TokenObject.breakListIntoTokens(tokenList, count) #objectify one line of tokens 

        return TokenObject.tokenObjectList

# myList = readOneLineAtATime()
# for item in myList:
    # print(item.value)
    # print("Value: " + str(item.value) + " Line: " + str(item.line))
