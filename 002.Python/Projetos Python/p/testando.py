diagonal_l = []
cont = 26
f_list = [26, 26]

for i in range(f_list[0] - 1, 0, -1):
    palavra_diagonal_l = ""
    for a in range(0, min(cont, f_list[1] - 1)):
        palavra_diagonal_l += f"{i+a}-{a} "
    cont -= 1
    diagonal_l.append(palavra_diagonal_l)