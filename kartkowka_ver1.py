import ...... #zaimportuj bibliotekę, która zawiera funkcję losującą liczby całkowite

....=input("Jak masz na imię? ") #nazwij zmienną, do której zostanie zapisane imię podane przez użytkownika
print("Cześć", ....) #wprowadź zmienną, do której zostało zapisane imię podane przez użytkownika
wiek=...(input("Ile masz lat? ")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą

wiekKomputera=.................... #wylosuj liczbę z zakresu od 1 do 40

while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 40)

if ................... #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jestem od Ciebie starszy!")
else:
    print("Jestem od Ciebie młodszy!")

szanse=3
while szanse>0:
    zgadywanie=int(.....("Zgadnij, ile mam lat! (masz trzy szanse)")) #wpisz funkcję, która pozwala pobrać coś od użytkownika
    ............................. #jeżeli zgadywanie jest równe wiekKomputera
        print("Tak, mam tyle lat!")
        exit()
    .............................. #ale jeżeli zgadywanie jest większe od wiekKomputera
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    ..... #w przeciwnym razie
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    ............. #jeżeli szanse są równe 0
        print("Nie udało Ci się!")

