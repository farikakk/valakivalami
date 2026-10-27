

# az eredeti szoveg megadasa
szoveg = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

# szotar letrehozasa az ekezetek cserelesehez
ekezetek = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 'ú': 'u', 'ü': 'u', 'ű': 'u',
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ö': 'O', 'Ő': 'O', 'Ú': 'U', 'Ü': 'U', 'Ű': 'U'
}

# ures valtozo az uj szovegnek
ascii_szoveg = ""

# vegigmegyunk a szoveg minden egyes betujen
for karakter in szoveg:
    # a get fuggveny visszaadja az ekezet nelkuli betut, ha benne van a szotarban
    # ha nincs benne (pl. masssalhangzok, szokozok), akkor az eredeti karaktert hagyja meg
    ascii_szoveg += ekezetek.get(karakter, karakter)

# kiiratjuk a vegeredmenyt
print(ascii_szoveg)