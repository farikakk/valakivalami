def f1():
    # nagybetusit es felkialtojelet rak a vegere
    return [s.upper() + '!' for s in ['auto', 'villamos', 'metro']]


def f2():
    # csak a kezdotetut csinalja nagyra
    return [s.capitalize() for s in ['aladar', 'bela', 'cecil']]


def f3():
    # csinal egy tizelemu listat csupa nullaval
    return [0 for _ in range(10)]


def f4():
    # megduplazza a szamokat egytol tizesig
    return [x * 2 for x in range(1, 11)]


def f5():
    # atalakitja a szoveges szamokat igazi szamokka
    sztring_szamok = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return [int(x) for x in sztring_szamok]


def f6():
    # szetszedi a szamot szamjegyekre
    szam_sztring = "1234567"
    return [int(j) for j in szam_sztring]


def f7():
    # megszamolja milyen hosszuak a szavak a mondatban
    mondat = 'The quick brown fox jumps over the lazy dog'
    return [len(szo) for szo in mondat.split()]


def f8():
    # kiszedi a szavak elso betujet
    mondat = "python is an awesome language"
    return [szo[0] for szo in mondat.split()]


def f9():
    # parokba rakja a szavakat meg a hosszukat
    mondat = 'The quick brown fox jumps over the lazy dog'
    return [(szo, len(szo)) for szo in mondat.split()]


def f10():
    # kigyujti a paros szamokat tiz alatt
    return [x for x in range(10) if x % 2 == 0]


def f11():
    # a husz alatti szamokbol a paros negyzeteket adja vissza
    return [x**2 for x in range(20) if (x**2) % 2 == 0]


def f12():
    # negyre vegzodo negyzetszamok husz alatt
    return [x**2 for x in range(20) if (x**2) % 10 == 4]


def f13():
    # osszerakja az angol abc nagybetuit egy szovegge
    return "".join([chr(i) for i in range(65, 91)])


def f14():
    # leszedi a felesleges szokozoket a szavakrol
    lista = ['  apple ', '     banana  ', '  kiwi']
    return [s.strip() for s in lista]


def f15():
    # egybe fuzi a lista szamjegyeit egy szovegbe
    szamjegyek = [1, 0, 1, 1, 0, 1, 0, 0]
    return "".join([str(j) for j in szamjegyek])

def main():
    # kiprobalja a harmadik fuggvenyt
    print(f3())

if __name__ == '__main__':
    main()