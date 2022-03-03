liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

""" if liczba1==liczba2:
    print("Liczby ",liczba1, "i", liczba2, "są równe.")
else:
    roznica=liczba1-liczba2
    print(roznica) """

def czy_rowne(a, b):
    if a==b:
        return "liczby są równe"
    else:
        return a-b

print(czy_rowne(liczba1, liczba2))