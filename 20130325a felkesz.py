class verem:
    def __init__(self):
        self._adatok = []

    def ures(self):
        return len(self._adatok) == 0

    def betesz(self, elem):
        self._adatok.append(elem)

    def kivesz(self):
        if self.ures():
            return None
        return self._adatok.pop()

    def meret(self):
        return len(self._adatok)

    def __str__(self):
        return "[" + " ".join(str(x) for x in self._adatok)


class MyQueue:
    def __init__(self):
        # ket verem letrehozasa
        self.v1 = verem()
        self.v2 = verem()

    def append(self, elem):
        # sor vegere rakja
        self.v1.betesz(elem)

    def is_empty(self):
        return self.v1.ures() and self.v2.ures()

    def size(self):
        return 0

    def popleft(self):
        # atpakolas meg felkesz
        if self.v2.ures():
            while not self.v1.ures():
                self.v2.betesz(self.v1.kivesz())
        return 0


def main():
    # teszt
    q = MyQueue()
    q.append(10)
    q.append(20)
    print(q.is_empty())
    print(q.size())
    print(q.popleft())


if __name__ == "__main__":
    main()
