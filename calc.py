print("Podaj pierwszą liczbę:")
x=int(input())
print("Podaj drugą liczbę:")
y=int(input())

print("Wskaż jakie działanie chcesz wykonać:\n")
print("+ -> dodawanie\n")
print("- -> odejmowanie\n")
print("* -> mnożenie\n")
print("/ -> dzielenie\n")
dzialanie=input()

if dzialanie=="+":
    wynik=x+y
    print(wynik)
elif dzialanie=="-":
    wynik=x-y
    print(wynik)
elif dzialanie=="*":
    wynik=x*y
    print(wynik)
elif dzialanie=="/":
    if y==0:
        print("Nie można dzielić przez 0!")
    else:
        wynik=x/y
        print(wynik)
else:
    print("Nie można wykonać działania - podano nieprawidłowy znak")

#kalkulator z uzyciem slownika
def dodaj(a, b):
  return a + b
  
def odejmij(a, b):
  return a - b
  
def pomnoz(a, b):
  return a * b
  
def podziel(a, b):
  return a/b

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