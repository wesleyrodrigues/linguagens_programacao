import pyperclip 

strin = "L zdqw wr glh"
ns = ""
for i in strin:
    if(i == " "):
        ns += " "
    else:
        ns += chr(ord(i) - 3)

pyperclip.copy(ns)