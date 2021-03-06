import os
import JackTokenizer as jt
import CompilationEngineFinal as ce 
import SymbolTable as ST
import VMWriter
import FuncTable
import sys 
import ErrorWriting
import fileinput

# input=sys.argv[1]
input = '/Users/Elisabeth/Desktop/Compilers/Compiler/s2020x/Map.jack'

#if any other variable besides i uses increment, this needs to be updated
# with fileinput.FileInput(input, inplace=True) as file:
#         for line in file:
#             print(line.replace('++', '= i + 1'), end='')
#         file.close()

# with fileinput.FileInput(input, inplace=True) as file:
#         for line in file:
#             print(line.replace('--', '= i - 1'), end='')
#         file.close()

# with fileinput.FileInput(input, inplace=True) as file:
#         for line in file:
#             print(line.replace('<=', '%'), end='')
#         file.close()

# with fileinput.FileInput(input, inplace=True) as file:
#         for line in file:
#             print(line.replace('>=', '$'), end='')
#         file.close()

# with fileinput.FileInput(input, inplace=True) as file:
#         for line in file:
#             print(line.replace('!=', '!'), end='')
#         file.close()

fileList=[]
if os.path.isdir(input):
    if input.endswith('/'):
        input=input[:-1]
    os.chdir(input)
    for file in os.listdir('.'):
        if file.endswith('.jack'):
            fileList.append(file)
elif os.path.isfile(input):
    fileList=[input]
else:
    raise Exception("Input should be either a file name or a directory name!")

fntable = FuncTable.FuncTable()

for file in fileList:
    
    inpname = file.split('/')[-1].split('.')[0]
    outFile = inpname + '.vm' 
    tokenizer=jt.JackTokenizer(file)
    table = ST.SymbolTable()
    vm = VMWriter.VMWriter(outFile)
    print("---------------------------------------------------------------------------------------------")
    print ("Compiling {0}".format(inpname))
    compiler=ce.CompilationEngine(tokenizer, table, vm, inpname, fntable)
    compiler.CompileClass()

if not fntable.isemptyundec():
    for (a, b) in fntable.undecfnlist:
        raise Exception("Undefined function {0} in {1} class".format(b, a))

