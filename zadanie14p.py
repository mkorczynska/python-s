slowo=input("Podaj słowo: ")
licznik=0
for i in slowo:
    if i=="a":
        licznik+=1
print(f"W słowie {slowo} jest {licznik} liter 'a'")