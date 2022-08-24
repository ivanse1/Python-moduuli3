vuosi = int(input("Anna vuosiluku. "))
if vuosi%400==0 or (vuosi%100!=0 and vuosi%4==0):
    print("Annettu vuosi on karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi.")