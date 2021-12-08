import random

liczba=random.randint(1, 50)
strzal=int(input("Zgadnij liczbe: "))

if strzal<liczba:
    print("za malo")
elif strzal>liczba:
    print("za duzo")
else:
    print("tak, to ta liczba")
 
if strzal==liczba:
    print("Tak, to ta liczba")
elif strzal>liczba:
    print("za duzo")
else:
    print("za malo")