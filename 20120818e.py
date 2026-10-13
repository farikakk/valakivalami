def f_pe1():
    # osszeadja a harommal vagy ottel oszthatoakat ezerig
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


def main():
    # megmutatja az elso project euler feladat eredmenyet
    print(f_pe1())

if __name__ == '__main__':
    main()