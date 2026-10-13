def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    # kivalogatja az engedelyezett karaktereket a szovegbol
    return "".join([c for c in text if c in chars])

def main():
    # kiprobalja a fuggvenyt egy teszt szoval
    print(valid("Asvanyviz"))

if __name__ == '__main__':
    main()