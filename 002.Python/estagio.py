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
a = 192
print("\n" * 1000)
for i in range(1, 21):
	print("""=SE(B{0}="";"";SE(B{0}=10+{1};"Correto";"Errado"))""".format((a), i))
	a += 1