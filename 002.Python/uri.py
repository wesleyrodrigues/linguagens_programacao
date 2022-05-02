input()
lista = list(map(int, input().split()))
t = 0

if len(lista) == 1:
  t = 1
else:
  if lista[0] > lista[1]:
    for i in range(1, (len(lista) - 1)):
      if i % 2 != 0:
        if not(lista[i] < lista[i+1]):
          t = 0
          break
        else:
          t = 1
  elif lista[0] < lista[1]:
    for i in range(1, (len(lista) - 1)):
      if i % 2 != 0:
        if not(lista[i] > lista[i+1]):
          t = 0
          break
        else:
          t = 1
  else:
    t = 0

print(t)