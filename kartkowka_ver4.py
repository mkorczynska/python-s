...... random #wpisz słowo, dzięki któremu zaimportujesz bibliotekę random

imie=.....("Jak masz na imię? ") #podaj funkcję, która pozwala pobrać coś od użytkownika
print(f"Cześć ......") #wpisz w odpowiedni sposób nazwę zmiennej imie, aby wyświetlić imię użytkownika
wiek=int(input("Ile masz lat? "))

wiekKomputera=random.randint...... #podaj zakres losowania (od 1 do 20)
while wiekKomputera==wiek:
    wiekKomputera=random.randint...... #podaj zakres losowania (od 1 do 20)

if ................... #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jesteś ode mnie starszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie
else:
    print("...........................") #wprowadź komunikat jaki powinien zostać wypisany, jeżeli warunek z if nie został spełniony

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat!"))
    ............................. #jeżeli zgadywanie jest równe wiekKomputera to
        print("Tak, właśnie tyle mam lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    .............................. #ale jeżeli zgadywanie jest mniejsze od wiekKomputera to
        print("Mam więcej lat!")
        exit()
    ..... #w przeciwnym razie
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    ............. #jeżeli szanse są równe 0
        print("Nie udało Ci się odgadąć mojego wieku!")