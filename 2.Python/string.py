x = 10
str(10)                     # '10'
ord("A")                    # 65
chr(65)                     # 'A'
len("casa")                 # 4
eval("x + 10")              # 20

format(10, "x")             # 'a'
format(1555, "o")           # '3023'
format(15, "E")             # '1.500000E+01'
format(1555, "F")           # '1555.000000'

hex(255)                      # '0xff'
oct(8)                      # '0o10'

'%#x' % 255, '%x' % 255, '%X' % 255                   # ('0xff', 'ff', 'FF')
format(255, '#x'), format(255, 'x'), format(255, 'X') # ('0xff', 'ff', 'FF')
f'{255:#x}', f'{255:x}', f'{255:X}'                   # ('0xff', 'ff', 'FF')

'%#o' % 10, '%o' % 10               # ('0o12', '12')
format(10, '#o'), format(10, 'o')   # ('0o12', '12')
f'{10:#o}', f'{10:o}'               # ('0o12', '12')

################################################################
# new
################################################################

"exemplo".capitalize()              # 'Exemplo'
"LeArN".lower()                     # 'learn'
"learn".upper()                     # 'LEARN'
"LeArN".swapcase()                  # 'lEaRn'
"learn".title()                     # 'Learn'
"learn".replace("l", "D")           # 'Dearn'   -> Troca uma letra por outra
"1".zfill(3)                        # '001' -> Adiciona zeros(0) na frente da string até tamanho definido
"   space   ".strip()               # 'space'
   "space".strip("sep")             # 'ac'


"learn python".split()              # ['learn', 'python']

"az09".isalnum()                    # True -> aA até zZ and 0 até 9 -> "." -> False
"az".isalpha()                      # True -> aA até zZ -> "1" -> False
"10.0".isdecimal()                  # False -> "10" -> True
"1".isdigit()                       # True -> "1.0" False
"learn".isidentifier()              # True ????
"learn".islower()                   # True
"10.0".isnumeric()                  # False -> "10" -> True
"learn".isprintable()               # True
" ".isspace()                       # True
"Learn".istitle()                   # True
"LEARN".isupper()                   # True

"12345".ljust(10, "0") # considera o tamanho da string e completa
"12345".rjust(10, "0") # mesmo que anterior só que adiciona na frente
" ".join(["1", "2", "3"]) # 1 2 3

str.casefold()
str.center(width[, fillchar])
str.count(sub[, start[, end]])
str.encode(encoding="utf-8", errors="strict")
str.endswith(suffix[, start[, end]])
str.expandtabs(tabsize=8)
str.find(sub[, start[, end]])
str.format(*args, **kwargs)
str.format_map(mapping)
str.index(sub[, start[, end]])
str.lstrip([chars])
str.partition(sep)
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rpartition(sep)
str.rsplit(sep=None, maxsplit=-1)
str.rstrip([chars])
str.splitlines([keepends])
str.startswith(prefix[, start[, end]])
str.translate(table)


'#'	-> The value conversion will use the “alternate form” (where defined below).
'0'	-> The conversion will be zero padded for numeric values.
'-'	-> The converted value is left adjusted (overrides the '0' conversion if both are given).
' '	-> (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
'+'	-> A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).

'd'	-> Signed integer decimal.	 
'i'	-> Signed integer decimal.	 
'o'	-> Signed octal value.	
'u'	-> Obsolete type – it is identical to 'd'.	
'x'	-> Signed hexadecimal (lowercase).	
'X'	-> Signed hexadecimal (uppercase).	
'e'	-> Floating point exponential format (lowercase).	
'E'	-> Floating point exponential format (uppercase).	
'f'	-> Floating point decimal format.	
'F'	-> Floating point decimal format.	
'g'	-> Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	
'G'	-> Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	
'c'	-> Single character (accepts integer or single character 
'r'	-> String (converts any Python object using repr()).	
's'	-> String (converts any Python object using str()).	
'a'	-> String (converts any Python object using ascii()).	
'%'	-> No argument is converted, results in a '%' character in 
