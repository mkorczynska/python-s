...... random #zaimportuj bibliotekę, która zawiera funkcję losującą liczby całkowite

imie=input("Jak masz na imię? ")
.....("Cześć", imie) #użyj funkcji, która wypisze powitanie
....=int(input("Ile masz lat? ")) #wprowadź nazwę zmiennej, do której przypisany zostanie wiek podany przez użytkownika

wiekKomputera=.................... #wylosuj liczbę z zakresu od 1 do 60
while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 60)

if ................... #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jestem od Ciebie młodszy!")
else:
    print("Jestem od Ciebie starszy!")

szanse=3
while szanse>0:
    zgadywanie=...(input("Zgadnij, ile mam lat!")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą
    ............................. #jeżeli zgadywanie jest większe od wiekKomputera
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    .............................. #ale jeżeli zgadywanie jest mniejsze od wiekKomputera
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    ..... #w przeciwnym razie
        print("Tak, mam tyle lat!")
        exit()

    ............. #jeżeli szanse są równe 0
        print("Nie udało Ci się!")

