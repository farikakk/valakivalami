def normalize(szoveg):
    return szoveg

def anagramma_szotar(szo1, szo2):
    norm1 = szo1.lower().replace(" ", "")
    norm2 = szo2.lower().replace(" ", "")
    
    # ha eleve nem egyenlo a hosszuk, nem lehetnek anagrammak
    if len(norm1) != len(norm2):
        return False
        
    # szotar letrehozasa a betuk szamolasahoz
    betu_szamlalo = {}
    
    # elso szo betuinek megszamolasa
    for betu in norm1:
        betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1
        
    # masodik szo betuinek ellenorzese es levonasa
    for betu in norm2:
        # ha olyan betut talalunk, ami nincs a szotarban, nem anagramma
        if betu not in betu_szamlalo:
            return False
            
        betu_szamlalo[betu] -= 1
        
        # ha valamelyik betubol tobb van a masodik szoban, mint az elsoben
        if betu_szamlalo[betu] < 0:
            return False
            
    # ha minden stimmel, a ket szo anagramma
    return True


# tesztek futtatasa a peldak alapjan
print(anagramma_szotar("listen", "silent"))                           
print(anagramma_szotar("A gentleman", "Elegant man"))                 
print(anagramma_szotar("Clint Eastwood", "Old west action"))          
print(anagramma_szotar("dormitory", "dirty room"))                    
print(anagramma_szotar("étel", "élet"))                               
print(anagramma_szotar("kolostor", "rostokol"))                       
print(anagramma_szotar("alma", "korte"))