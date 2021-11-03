import random

liczba=random.randint(1, 20)
print(liczba)
strzal=int(input("Jaką liczbę wylosował komputer?"))

proby = []
proby.append(strzal)

if strzal==liczba and len(proby)==1:
    print(f"Brawo. Do odgadnięcia liczby potrzebowałeś {len(proby)} prób.")
else:
    while strzal!=liczba:
        proby.append(strzal)
        strzal=int(input("Spróbuj jeszcze raz. Jaką liczbę wylosował komputer?"))
        if strzal==liczba:
            print(f"Brawo. Do odgadnięcia liczby potrzebowałeś {len(proby)} prób.")