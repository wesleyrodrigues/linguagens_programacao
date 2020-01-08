a = "blablablablbablslbs"
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
# List is too long (19 elements, expected <= 10)

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
# / valores c and d podem ser posicionais ou não
# * valores e and f devem ser posicionais

f(10, 20, 30, d=40, e=50, f=60) # tá mais o que significa posicional?? 
# só sei que são essas letrinhas aí