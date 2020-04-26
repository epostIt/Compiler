import fileinput
import re

FILE_PATH = '/Users/Elisabeth/Desktop/Compilers/Compiler/text.txt'
delimiters = r'([\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|(?:"[^"]*")| *)'
comment=r'(?:(\/\*(.|\n)*?\*\/)|(//.*))'
array = ['class', 'Main', '{']
#what if I read in one line of tokens at a time, tokenize them, attach them to a line number, then increment line and count


def readOneLineAtATime():
    totalList = []
    with fileinput.input(files=(FILE_PATH)) as f:
        count = 0
        for line in f:  
            inp = " ".join(re.sub(comment,"",line).split())
            tokenList=[token for token in re.split(delimiters,inp) if token not in ('', ' ')]
            # print(tokenList)
            totalList = totalList + tokenList
            count = count + 1
            # print(count)
            TokenObject.breakListIntoTokens(tokenList, count)

        # print(totalList)
        


class TokenObject:

    def __init__(self, token, line):
        self.line = line
        self.value = token

    def breakListIntoTokens(tokenList, line):
        for token in tokenList:
            ob = TokenObject(token, line)
            tokenObjectList.append(ob)
            # print(ob.line)
            # print(ob.value)

tokenObjectList = []
readOneLineAtATime()
# testOb = tokenObjectList[5]
for item in tokenObjectList:
    print("Value: " + str(item.value) + " Line: " + str(item.line))
