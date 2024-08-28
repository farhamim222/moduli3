pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamaara = 37

if pituus < alamaara:

    puuttuu = alamaara - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Kuhan pituudesta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun mittainen. Voit pitää kuhan.")
