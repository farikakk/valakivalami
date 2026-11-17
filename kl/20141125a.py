# ------------------------------------------------------------
# 20141125a - verem (stack) es sor (queue) adatszerkezetek
# megvalositasa sajat osztalyokkal, tesztekkel egyutt
# ------------------------------------------------------------


class verem:
    # lifo (last in, first out) elven mukodo verem adatszerkezet

    def __init__(self, kezdo_elemek=None):
        # belso lista az elemek tarolasara
        self._adatok = []
        # ha kaptunk kezdo elemeket, egyenkent betesszuk oket
        if kezdo_elemek is not None:
            for elem in kezdo_elemek:
                self.betesz(elem)

    def ures(self):
        # igazat ad vissza, ha nincs egyetlen elem sem a veremben
        return len(self._adatok) == 0

    def betesz(self, elem):
        # uj elem elhelyezese a verem tetejere
        self._adatok.append(elem)

    def kivesz(self):
        # a verem tetejen levo elem eltavolitasa es visszaadasa
        # ures verem eseten none ertekkel ter vissza
        if self.ures():
            return None
        return self._adatok.pop()

    def teteje(self):
        # megmutatja a verem tetejen levo elemet kivetel nelkul
        if self.ures():
            return None
        return self._adatok[-1]

    def meret(self):
        # visszaadja a veremben talalhato elemek darabszamat
        return len(self._adatok)

    def kiurit(self):
        # torli az osszes elemet a verembol
        self._adatok.clear()

    def __len__(self):
        # tamogatja a beepitett len() fuggveny hasznalatat
        return self.meret()

    def __bool__(self):
        # logikai vizsgalatnal (pl. if v:) igaz, ha nem ures a verem
        return not self.ures()

    def __str__(self):
        # a feladatban megadott formatumu szoveges megjelenites
        tartalom = " ".join(str(elem) for elem in self._adatok)
        return "[" + tartalom

    def __repr__(self):
        # fejlesztoi megjelenites hibakereseshez
        return f"verem({self._adatok!r})"


class sor:
    # fifo (first in, first out) elven mukodo sor adatszerkezet

    def __init__(self, kezdo_elemek=None):
        # belso lista a sor elemeinek tarolasara
        self._adatok = []
        # ha kaptunk kezdo elemeket, sorrendben betesszuk oket
        if kezdo_elemek is not None:
            for elem in kezdo_elemek:
                self.betesz(elem)

    def ures(self):
        # igazat ad vissza, ha a sor jelenleg ures
        return len(self._adatok) == 0

    def betesz(self, elem):
        # uj elem beallitasa a sor legvegere
        self._adatok.append(elem)

    def kivesz(self):
        # a sor elejen varakozo legregebbi elem kivetele es visszaadasa
        # ures sor eseten none ertekkel ter vissza
        if self.ures():
            return None
        return self._adatok.pop(0)

    def elso(self):
        # visszaadja a sor elejen levo elemet eltavolitas nelkul
        if self.ures():
            return None
        return self._adatok[0]

    def meret(self):
        # visszaadja a sorban varakozo elemek szamat
        return len(self._adatok)

    def kiurit(self):
        # kiuriti a teljes sort
        self._adatok.clear()

    def __len__(self):
        # tamogatja a beepitett len() fuggveny hasznalatat
        return self.meret()

    def __bool__(self):
        # logikai vizsgalatnal (pl. if s:) igaz, ha van elem a sorban
        return not self.ures()

    def __str__(self):
        # szoveges megjelenites a sor elejetol a vegeig
        tartalom = " ".join(str(elem) for elem in self._adatok)
        return "[" + tartalom + "]"

    def __repr__(self):
        # fejlesztoi megjelenites hibakereseshez
        return f"sor({self._adatok!r})"


def teszt_verem():
    # a feladatban szereplo verem peldakod futtatasa
    print("=== verem tesztelese ===")
    v = verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


def teszt_sor():
    # a sor adatszerkezet mukodesenek ellenorzese
    print("=== sor tesztelese ===")
    s = sor()
    print(s)
    print(s.ures())
    s.betesz(10)
    s.betesz(20)
    s.betesz(30)
    print(s)
    print(s.meret())
    print(s.ures())
    print("sor elejen:", s.elso())
    x = s.kivesz()
    print("kivett elem:", x)
    print(s)
    s.kivesz()
    s.kivesz()
    x = s.kivesz()
    print("ures sorbol kivett:", x)


def teszt_extra_muveletek():
    # kiegeszito metodusok es magic methodok tesztelese
    print("=== kiegeszito muveletek ===")
    v = verem([7, 8, 9])
    print("kezdo verem:", repr(v), "hossz:", len(v), "teteje:", v.teteje())
    if v:
        print("a verem nem ures (truthy)")
    v.kiurit()
    print("kiurites utan ures:", v.ures())

    s = sor(["elso", "masodik", "harmadik"])
    print("kezdo sor:", repr(s), "hossz:", len(s), "elso:", s.elso())
    if s:
        print("a sor nem ures (truthy)")
    s.kiurit()
    print("kiurites utan ures:", s.ures())


def main():
    # osszes tesztfuggveny meghivasa elvalasztokkal
    teszt_verem()
    print("-" * 40)
    teszt_sor()
    print("-" * 40)
    teszt_extra_muveletek()


if __name__ == "__main__":
    main()
