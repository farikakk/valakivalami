def munchhausen_check(n):
    # ellenorzi hogy a megadott szam munichhausen-e
    if n == 0:
        return True
    orig = n
    s = 0
    while n > 0:
        d = n % 10
        if d != 0:
            s += d**d
        n //= 10
    return s == orig


def f1():
    # megkeresi a tiz ezer alattiakat gyorsan
    return [x for x in range(10000) if munchhausen_check(x)]


def f2():
    # vegignez mindent negy szaznegyven millioig
    return [x for x in range(440_000_000) if munchhausen_check(x)]

def main():
    # eredmeny printelese
    print(f1())

if __name__ == '__main__':
    main()