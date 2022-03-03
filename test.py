import random

slowa=[]

f = open("python-s\slownik.txt", "r")
for x in f:
    x=x.strip()
    slowa.append(x)

f.close()

imie_gracza=input("Podaj swoje imie:")
imie_komputera="Teodor"

print("Zaczynamy grę.")
pierwsza_litera=random.choice("abcdefghijklmnoprstuwz")
print("Litera, od której zaczniemy to:", pierwsza_litera)
los_komputera=random.randint(1, 6)
los_gracza=random.randint(1, 6)

while los_komputera==los_gracza:
    los_komputera=random.randint(1, 6)
    los_gracza=random.randint(1, 6)

if los_gracza>los_komputera:
    print("zaczyna gracz o imieniu", imie_gracza)
    print("pierwsza litera to", pierwsza_litera)
    slowo=input("Podaj slowo rozpoczynające się na tę literę: ")
elif los_gracza<los_komputera:
    print("zaczyna komputer o imieniu", imie_komputera)
    slowo=random.choice(slowa)
    while slowo[0]!=pierwsza_litera:
        slowo=random.choice(slowa)
