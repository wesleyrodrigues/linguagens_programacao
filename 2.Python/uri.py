lista0 = []
for i in range(0, int(input())):
    s = input()
    lista = [s[2:4], s[5:8], s[-2:]]
    n = 0

    for i in lista:
        if len(i) == 3:
            if not(i[1].isdigit()):
                for a in [n for n in i if n.isdigit()]:
                    n += int(a)
            else:
                n += int("".join([l for l in i if l.isdigit()]))
        else:
            n += int("".join([l for l in i if l.isdigit()]))
    lista0.append(n)

for i in range(0, len(lista0)):
    print(lista0[i])
