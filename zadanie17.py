import random
slowa=["absztyfikant", "relatywizm", "koperek"]

zycia=5

zgadywane=random.choice(slowa)   
dlugosc=len(zgadywane)
tablica=["_"]*dlugosc
while zycia>0:
    print(*tablica)
    litera=input("Podaj literę: ")
    if litera in zgadywane:
        print("Jest")
        for i in range(dlugosc):
            if zgadywane[i] == litera:
                tablica[i]=litera
    else:
        print("nie ma!")
        zycia-=1

    if "_" not in tablica:
        print("EPIC WIN")
        exit()
    elif zycia==0:
        print("Przegrywem się jest, a nie bywa")
        exit()