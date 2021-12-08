liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

dzialanie=input("Podaj działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie")

if dzialanie=="+":
    wynik=liczba1+liczba2
    print("Wynik dodawania to", wynik)
elif dzialanie=="-":
    wynik=liczba1-liczba2
    print("Wynik odejmowania to", wynik)
elif dzialanie=="*":
    wynik=liczba1*liczba2
    print("Wynik mnożenia to", wynik)
elif dzialanie=="/":
    if liczba2==0:
        print("Nie można dzielić przez 0")
    else:
        wynik=liczba1/liczba2
        print("Wynik dzielenia to", wynik)
else:
    print("Zły znak")
