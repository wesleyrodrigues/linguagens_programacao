import pyperclip
# st = input()
# while(st != '0'):
#     st = input()
#     if(len(st) == 3):
#         print("{} centena(s) {} dezena(s) {} unidade(s)".format(
#             st[0], st[1], st[2]))
#     elif(len(st) == 2):
#         print("0 centena {} dezena(s) {} unidade(s)".format(st[0], st[1]))
#     elif(len(st) == 1):
#         print("0 centena 0 dezena {} unidade(s)".format(st[0]))
# a = 192
# print("\n" * 1000)
# for i in range(1, 21):
# 	print("""=SE(B{0}="";"";SE(B{0}=10+{1};"Correto";"Errado"))""".format((a), i))
# 	a += 1
stTotal = ""

for i in range(2, 36):
	st1 = "=SE(E(MÊS(B{0})=MÊS(E2);DIA(E2)=DIA(B{0}));".format(i)
	st2 = "\"Niver Chegou\";"
	st3 = "SE(OU(E(MÊS(B{0})=MÊS(E2);".format(i)
	st4 = "DIA(B{0}) > DIA(E2)); MÊS(B{0})=MÊS(E2)+1);".format(i)
	st5 = "\"Niver Chegando\";\"\"))\n"
	stTotal += st1 + st2 + st3 + st4 + st5

pyperclip.copy(stTotal)

"=SE(MÊS(B{0})=MÊS(F2);\"Mês atual\";SE(MÊS(B{0})<MÊS(F2);\"Já passou\";\"\"))".format(i)

