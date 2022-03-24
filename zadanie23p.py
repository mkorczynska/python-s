liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

def czy_rowne(a, b):
    if a==b:
        return "liczby są równe"
    else:
        return a-b

print(czy_rowne(liczba1, liczba2))