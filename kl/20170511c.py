class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # logikai vizsgalatnal (pl. if r1:) hivodik meg
    def __bool__(self):
        return self.area() > 0

    # kisebb (<) operator
    def __lt__(self, other):
        return self.area() < other.area()

    # egyenloseg (==) operator
    def __eq__(self, other):
        return self.area() == other.area()

    # osszeadas (+) operator: ket teglalapbol uj teglalapot csinal
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    # szoveges megjelenites print() eseten
    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


def main():
    r1 = Rectangle(0, 5)
    r2 = Rectangle(10, 20)

    # logikai ertek tesztelese (__bool__)
    if r1:
        print("r1 is considered to be true (truthy)")
    else:
        print("r1 is considered to be false (falsy)")

    print("-" * 20)

    # kisebb operator tesztelese (__lt__)
    print(r1 < r2)
    print(r2 < r1)

    print("-" * 20)

    # egyenloseg es osszeadas tesztelese (__eq__, __add__)
    r3 = Rectangle(5, 40)
    print(r2 == r3)
    r4 = r1 + r2
    print(r4)


if __name__ == "__main__":
    main()
