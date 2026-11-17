from enum import Enum, auto


class Hangrend(Enum):
    MELY = auto()
    MAGAS = auto()
    VEGYES = auto()
    SEMMILYEN = auto()


MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"


def hangrend(szo):
    van_mely = False
    van_magas = False

    # kisbetusse alakitas a nagybetuk kezelesehez (pl. pfffffff)
    for c in szo.lower():
        if c in MELY_MGHK:
            van_mely = True
        elif c in MAGAS_MGHK:
            van_magas = True

    # hangrend eldontese a talalt maganhangzok alapjan
    if van_mely and van_magas:
        return Hangrend.VEGYES
    elif van_mely:
        return Hangrend.MELY
    elif van_magas:
        return Hangrend.MAGAS
    else:
        return Hangrend.SEMMILYEN


def main():
    # peldaszavak tesztelese
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for w in words:
        print(f"{w} -> {hangrend(w)} ({hangrend(w).name})")


if __name__ == "__main__":
    main()
