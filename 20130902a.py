
def median(szamok):
    # eloszor sorba rendezzuk a listat, mivel a medianhoz ez elengedhetetlen
    rendezett = sorted(szamok)
    n = len(rendezett)
    
    # ha a szamok darabszama paratlan
    if n % 2 != 0:
        # a kozepso erteket adjuk vissza
        # a dupla perjel (//) egesz osztast jelent, igy megkapjuk a kozepso indexet
        return rendezett[n // 2]
    # ha a szamok darabszama paros
    else:
        # a ket kozepso elemet vesszuk, majd ezek atlagat szamoljuk ki
        kozep_bal = rendezett[n // 2 - 1]
        kozep_jobb = rendezett[n // 2]
        return (kozep_bal + kozep_jobb) / 2

# tesztek futtatasa a megadott peldak alapjan
print(median([1, 2, 3, 4, 5]) == 3)
print(median([3, 1, 2, 5, 3]) == 3)
print(median([1, 300, 2, 200, 1]) == 2)
print(median([3, 6, 20, 99, 10, 15]) == 12.5)