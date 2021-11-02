import math
def dodaj(a, b):
  return a + b
  
def odejmij(a, b):
  return a - b
  
def pomnoz(a, b):
  return a * b
  
def podziel(a, b):
  return a/b

def poteguj(a, b):
    return pow(a, b)

def hypotuj(a, b):
    return math.hypot(a, b)

dzialania={"+": dodaj, "-": odejmij, "*": pomnoz, "/": podziel, "^": poteguj, "hyp": hypotuj }

a = int(input("Podaj pierwszą liczbę: "))
dzialanie = str(input("Jakie działanie chcesz wykonać? \n + \n - \n * \n / \n ^\n hyp\n"))
b = int(input("Podaj drugą liczbę: \n"))

obliczenia = dzialania[dzialanie]
wynik = obliczenia(a, b)

if dzialanie == "hyp":
    print(f"Wykonane przez Ciebie działanie to: hypot({a}, {b})={wynik}")
else:
    print(f"Wykonane przez Ciebie działanie to: {a} {dzialanie} {b} = {wynik}")