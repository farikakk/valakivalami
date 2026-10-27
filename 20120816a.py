def kiralyno_rajzolo(poziciok):
    print("+-----------------+")
    
    for r in range(7, -1, -1):
        sor_elemek = []
        
        for c in range(8):
            if poziciok[c] == r:
                sor_elemek.append("Q")
            else:
                sor_elemek.append(".")
        
        sor_szoveg = "| " + " ".join(sor_elemek) + " |"
        print(sor_szoveg)
        
    print("+-----------------+")

# teszteles a peldaban megadott listaval
kiralyno_rajzolo([0, 4, 7, 5, 2, 6, 1, 3])