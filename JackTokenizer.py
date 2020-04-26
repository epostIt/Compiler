import re
import fileinput
symbols = r'()[]{},;=.+-*/&|~<>'
comment=r'(?:(\/\*(.|\n)*?\*\/)|(//.*))'
delimiters = r'([\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|(?:"[^"]*")| *)'
delim = re.compile('([\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|(?:"[^"]*")| *)')
keywords = ('class','constructor','method','function','int','boolean','char','void','var','static','field','let','do','if','else','while','return','true','false','null','this')

FILE_PATH = '/Users/Elisabeth/Desktop/Compilers/Compiler/error.jack'

class JackTokenizer(object):
	
	def __init__(self, inputFile):
		self.currLine=-1
		self.token=None
		# fin=open(inputFile,"r+")
		# self.inp=fin.read()
		# self.inp = " ".join(re.sub(comment,"",self.inp).split()) 
		# self.tokenList=[token for token in re.split(delimiters,self.inp) if token not in ('', ' ')]
		self.tokenList = TokenObject.readOneLineAtATime()
		# for item in self.tokenList:
    	# 		print("Value: " + str(item.value) + " Line: " + str(item.line))


	def advance(self):
		item = self.tokenList.pop(0)
		self.token=item.value
		# self.token = self.tokenList.pop(0)
		# print(self.token)

	def hasMoreTokens(self):
		if len(self.tokenList)>0:
			return True
		return False

	def tokenType(self):
		if self.token in keywords: 
			return('KEYWORD')
		elif self.token in symbols:
			return('SYMBOL')
		elif self.token.isdigit():
			if(int(self.token)>=0 and int(self.token)<=32767):
				return('INT_CONST')
			else:
				raise Exception('Integer constant should be between 0 and 32767, it is %s' % self.token)
		elif re.match(r'(?:"[^"]*")', self.token):
			return('STRING_CONST')
		elif re.match(r'^[\w\d_]*$', self.token) and not self.token[0].isdigit() and self.token not in keywords:
			return('IDENTIFIER')
		else:
			raise Exception('Illegal Token: %s' %self.token)


	def keyword(self):
		return self.token

	def symbol(self):
		return self.token

	def identifier(self):
		return self.token

	def intVal(self):
		return int(self.token)

	def stringVal(self):
		return self.token[1:-1]


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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