""" dzialanie=""
while dzialanie!="0":
    dzialanie=input("Podaj działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie, 0-koniec")
    if dzialanie=="+": #jeżeli uzytkownik wybral +
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1+liczba2
        print("Wynik dodawania to", wynik)
    elif dzialanie=="-":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1-liczba2
        print("Wynik odejmowania to", wynik)
    elif dzialanie=="*":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1*liczba2
        print("Wynik mnożenia to", wynik)
    elif dzialanie=="/":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        if liczba2==0:
            print("Nie można dzielić przez 0")
        else:
            wynik=liczba1/liczba2
            print("Wynik dzielenia to", wynik)
    elif dzialanie=='0':
        break
    else:
        print("Błędny znak.") """

###############################################################
dzialanie=""
while dzialanie!="0":
    dzialanie=input("Podaj działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie, 0-koniec działania ")
    if dzialanie=="+": #jeżeli uzytkownik wybral +
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1+liczba2
        print("Wynik dodawania to", wynik)
    elif dzialanie=="-":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1-liczba2
        print("Wynik odejmowania to", wynik)
    elif dzialanie=="*":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=liczba1*liczba2
        print("Wynik mnożenia to", wynik)
    elif dzialanie=="/":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        if liczba2==0:
            print("Nie można dzielić przez 0")
        else:
            wynik=liczba1/liczba2
            print("Wynik dzielenia to", wynik)
    else:
        if dzialanie!="0":
            print("Błędny znak.")