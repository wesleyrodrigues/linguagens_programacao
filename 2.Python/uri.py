Triangulo = list(map(float, input().split()))
Triangulo.sort(reverse=True)
A, B, C = Triangulo

def rentangulo(A, B, C):
  if (A**2) == (B**2 + C**2):
    print("Retangulo: S")
  else:
    print("Retangulo: N")

if A >= (B + C):
    print("Invalido")
else:
  if A == B and B == C:
    print("Valido-Equilatero")
    rentangulo(A, B, C)
  elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
    print("Valido-Isoceles")
    rentangulo(A, B, C)
  elif (A != B and B != C and A != C):
    print("Valido-Escaleno")
    rentangulo(A, B, C)
    