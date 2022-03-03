def dodawanie(a, b):
    return a+b

def odejmowanie(a, b):
    return a-b

def mnozenie(a, b):
    return a*b

def dzielenie(a, b):
    if b==0:
        return "nie można dzielić przez 0"
    else:
        return a/b


dzialanie=input("Podaj działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie, 0-koniec działania ")
while dzialanie!="0":
    if dzialanie=="+":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=dodawanie(liczba1, liczba2)
        print("Wynik dodawania to", wynik)
        print("Wynik dodawania to...: ", dodawanie(liczba1, liczba2))
    elif dzialanie=="-":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=odejmowanie(liczba1, liczba2)
        print("Wynik odejmowania to", wynik)
    elif dzialanie=="*":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=mnozenie(liczba1, liczba2)
        print("Wynik mnożenia to", wynik)
    elif dzialanie=="/":
        liczba1=int(input("Podaj pierwszą liczbę: "))
        liczba2=int(input("Podaj drugą liczbę: "))
        wynik=dzielenie(liczba1, liczba2)
        print(wynik)
    else:
        if dzialanie!="0":
            print("Błędny znak.")
    dzialanie=input("Podaj działanie: + dodawanie, - odejmowanie, * mnożenie, / dzielenie, 0-koniec działania ")