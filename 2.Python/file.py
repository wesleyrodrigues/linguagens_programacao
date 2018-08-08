# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
import os

f = open("file.txt", "rt")
print(f.readline()) # teste1\n
print(f.readline()) # teste2\n
print(f.read()) # teste1\nteste2\nteste3 # não ser executado com readline!!
# caso contrário irá só ler o restante das linhas

for x in f:
    print(x, end="") # percorre por linha

f.close()
f = open("file.txt", "a")
# must have exactly one of create/read/write/append mode
f.write("teste4\nteste5\n")
f.close()
f = open("file.txt", "rt")
print(f.read()) # teste1\nteste2\nteste3\nteste4\nteste5
f.close()
f = open("file.txt", "w") # caso não haja arquivo cria um novo
f.write("teste1\nteste2\nteste3\n") # sobrescreve arquivo
f.close()

# os.remove("file.txt") # remove arquivo
# f = open("file.txt", "x") # cria novo arquivo se existe gera erro
# f.close()