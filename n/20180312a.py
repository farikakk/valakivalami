def main():
    # chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z') + 1))

    for c in codes:
        print(f"({c}, '{chr(c)}')")


if __name__ == '__main__':
    main()