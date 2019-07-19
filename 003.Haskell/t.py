e, d = input().split(" ")
e, d = int(e), int(d)

if(e <= d-3):
    print("Muito bem! Apresenta antes do Natal!")
elif(e > d):
    print("Eu odeio a professora!")
else:
    print("Parece o trabalho do meu filho!")
    e += 2
    if(e < 24):
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")