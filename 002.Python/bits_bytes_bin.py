# bits
x, y = 10, 5
x | y == 15
x ^ y == 15
x & y == 0
x << y == 320
x >> y == 0
~x == -11

bin(9)                           #'0b1001'

(9).bit_length()                   # 4  # ou (9).bit_length()
(9).to_bytes(2, byteorder='big')   # b'\x00\t'
