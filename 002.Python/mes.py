import pyperclip

def mes(dia_inicial, dias_mes):
    dias = ""
    for i in range(dia_inicial, dias_mes):
        dias += "{}/10/19\n".format(dia_inicial).zfill(9)
        dia_inicial += 7
        if(dia_inicial > dias_mes):
            break
    pyperclip.copy(dias)

mes(4, 31)