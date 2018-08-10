try:
    string = input()
    while string:
        v = 0
        promo, qtd_lata = string.split()
        promo, qtd_lata = int(promo), int(qtd_lata)
        
        for i in range(0, promo):
            bebi, reais = input().split()
            bebi, reais = int(bebi), int(reais)
            
            v_n = (qtd_lata // bebi) * reais
            
            if v_n > v:
                v = v_n
        
        print(v)
        string = input()

except EOFError:
    pass