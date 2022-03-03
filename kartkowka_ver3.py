............. #zaimportuj bibliotekę zawierającą funkcję do losowania

imie=.....("Jak masz na imię? ") #podaj funkcję, która pozwala pobrać coś od użytkownika
print("Cześć", imie)
wiek=...(input("Ile masz lat? ")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą

wiekKomputera=random.randint...... #podaj zakres losowania (od 1 do 30)
while wiekKomputera==wiek:
    wiekKomputera=random.randint...... #podaj zakres losowania (od 1 do 30)

if ................... #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    .....("Jestem od Ciebie starszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie
else:
    print("Jestem od Ciebie młodszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat! (masz trzy szanse)"))
    ............................ #jeżeli zgadywanie jest mniejsze od wiekKomputera to
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    ............................... #ale jeżeli zgadywanie jest równe wiekKomputera to
        print("Tak, mam tyle lat!")
        exit()
    ..... #w przeciwnym razie
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    ............. #jeżeli szanse są równe 0
        print("Nie udało Ci się!")