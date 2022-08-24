pituus = float(input("Anna kuhan pituus. "))
if pituus < 37:
    print("Kuhan lasketaan takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {37-pituus} senttiä.")