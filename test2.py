def dodaj(a, b):
    return a + b
  
def odejmij(a, b):
    return a - b
  
def pomnoz(a, b):
    return a * b
  
def podziel(a, b):
    return a/b

akcja="a"
while akcja!="KONIEC":
    akcja=input("Wybierz program: 1-kalkulator, 2-kalkulator pol, 3-info, KONIEC-koniec działania")
    if akcja=="1":
        print("Witaj w kalkulatorze")

        dzialania={"+": dodaj, "-": odejmij, "*": pomnoz, "/": podziel }

        a = int(input("Podaj pierwszą liczbę: "))
        dzialanie = str(input("Jakie działanie chcesz wykonać? \n + \n - \n * \n / \n "))
        b = int(input("Podaj drugą liczbę: \n"))

        while dzialanie == "/" and b==0:
            print(f"Działanie, które chcesz wykonać to dzielenie. Dzielnik nie może być równy 0. Podaj inną liczbę.")
            b = int(input("Podaj drugą liczbę: \n"))

        obliczenia = dzialania[dzialanie]
        wynik = obliczenia(a, b)
        print(f"Wykonane przez Ciebie działanie to: {a} {dzialanie} {b} = {wynik}")
    elif akcja=="2":
        print("Witaj w kalkulatorze pol")
    elif akcja=="3":
        print("Witaj w info")
        liczba=int(input("Podaj liczbe: "))
        
