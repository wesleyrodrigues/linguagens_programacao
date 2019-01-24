x = 10
y = 5

x + y == 15         # Adição
x - y == 5          # Subtração
x * y == 50         # Multiplicação
x / y == 2.0        # Divisão (float)
x // y == 2         # Divisão (inteira)
x % y == 0          # Resto da divisão
-x == -10           # operador negativo
+x == 10            # operador positivo
x ** y == 100000    # Elevação
x, y = 3, 4         # x = 3, y = 4
x, y = [3, 4]       # x = 3, y = 4
x, *y = [3, 4, 5]   # x = 3, y = [4, 5]

int(10.9)                           # 10
float(10)                           # 10.0
abs(-10)                            # 10 Retorna valor positivo
divmod(10, 2)                       # (5, 0) Retorna divisão e resto
pow(10, 2)                          # 100 -> 10**2
round(20.2834, 2)                   # 20.28

int.bit_length(6)    # 3 Retorna tamanho bit 7 bit = 110 => três números ou caracteres 
int.from_bytes(b'\x00\x10', byteorder='big')
int.from_bytes(b'\x00\x10', byteorder='little')
int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
int.from_bytes([255, 0, 0], byteorder='big')
int.__subclasses__()

float.as_integer_ratio()
float.is_integer()
float.fromhex('0x3.a7p10')
float.hex(3740.0)

##################################################################################
# new
##################################################################################