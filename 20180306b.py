def inverse_captcha_from_file(fajlnev="input.txt"):
    # beolvassa a fajlt es kiszamolja a captchat
    with open(fajlnev, "r", encoding="utf-8") as f:
        szamsor = f.read().strip()
    
    return sum(
        int(szamsor[i])
        for i in range(len(szamsor))
        if szamsor[i] == szamsor[(i + 1) % len(szamsor)]
    )

def main():
    # lefuttatja es kiirja az eredmenyt
    print(inverse_captcha_from_file())

if __name__ == '__main__':
    main()