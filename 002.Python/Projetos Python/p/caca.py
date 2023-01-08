f = open("p1.txt", "r")
f_list = list(f)

palavra = "OVO"
print("\n\n" + palavra + "\n")

for i in range(0, len(f_list)):
    if (palavra in f_list[i]):
        print(f"{i+1} - LINHA")
        print(f_list[i])
    elif (palavra in f_list[i][::-1]):
        print(f"{i+1} - LINHA INVERTIDA", end="")
        print(f_list[i][::-1])

coluna = []

for c in range(0, len(f_list[0]) - 1):
    palavra_coluna = ""
    for i in range(0, len(f_list)):
        palavra_coluna += f_list[i][c]
    coluna.append(palavra_coluna)

for i in range(0, len(coluna)):
    if (palavra in coluna[i]):
        print(f"{i+1} - COLUNA")
        print(coluna[i])
    elif (palavra in coluna[i][::-1]):
        print(f"{i+1} - COLUNA INVERTIDA")
        print(coluna[i][::-1])

diagonal_l = []
cont = 1

# 67 25
for i in range(len(f_list) - 1, 0, -1):
    palavra_diagonal_l = ""
    for a in range(0, min(cont, len(f_list[0]) - 1)):
        palavra_diagonal_l += f_list[i+a][a]
    cont += 1
    diagonal_l.append(palavra_diagonal_l)

for i in range(0, len(diagonal_l)):
    if (palavra in diagonal_l[i]):
        print(f"L - DIAGONAL 1")
        print(diagonal_l[i])
    elif (palavra in diagonal_l[i][::-1]):
        print(f"L - DIAGONAL 1 - INVERTIDA")
        print(diagonal_l[i][::-1])

print("\n\n")