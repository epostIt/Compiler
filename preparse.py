import fileinput

FILE_PATH = '/Users/Elisabeth/Desktop/Compilers/Compiler/error.jack'

with fileinput.FileInput(FILE_PATH, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('++', '=i+1'), end='')