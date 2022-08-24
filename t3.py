sukupuoli = input("Anna sukupuoli (N/M). ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l). "))
if sukupuoli == "N":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "M":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")