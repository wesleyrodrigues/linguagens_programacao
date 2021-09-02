#--coding:utf8;--
#qpy:console
import random, pyperclip

a = lambda x: chr(random.randint(x, 90)) 
st = ""
b = 40


for i in range(0, b):
    for i in range (0, b):
        st += "  " + a(65)
    st += "\n"

print(st)
pyperclip.copy(st)