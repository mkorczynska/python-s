slowo=input("Podaj słowo: ")

licznik=0
for litera in slowo:
    if litera=="a":
        licznik+=1

print(f"W słowie {slowo} jest {licznik} liter 'a'")