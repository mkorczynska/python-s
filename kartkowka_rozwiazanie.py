import random

imie=input("Jak masz na imię? ")
print("Cześć", imie)
wiek=int(input("Ile masz lat? "))

wiekKomputera=random.randint(1, 10)
while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 10)

if wiekKomputera>wiek:
    print("Jestem od Ciebie starszy!")
else:
    print("Jestem od Ciebie młodszy!")

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat! (masz trzy szanse)"))
    if zgadywanie==wiekKomputera:
        print("Tak, mam tyle lat!")
        exit()
    elif zgadywanie>wiekKomputera:
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    else:
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    if szanse==0:
        print("Nie udało Ci się!")

##########################################################################################
import random #zaimportuj bibliotekę, która zawiera funkcję losującą liczby całkowite

imie=input("Jak masz na imię? ")
print("Cześć", imie) #użyj funkcji, która wypisze powitanie
wiek=int(input("Ile masz lat? ")) #wprowadź nazwę zmiennej, do której przypisany zostanie wiek podany przez użytkownika

wiekKomputera=random.randint(1, 60) #wylosuj liczbę z zakresu od 1 do 60
while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 60)

if wiekKomputera<wiek: #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jestem od Ciebie młodszy!")
else:
    print("Jestem od Ciebie starszy!")

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat! (masz trzy szanse)")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą
    if zgadywanie>wiekKomputera: #jeżeli zgadywanie jest większe od wiekKomputera
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    elif zgadywanie<wiekKomputera: #ale jeżeli zgadywanie jest mniejsze od wiekKomputera
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    else: #w przeciwnym razie
        print("Tak, mam tyle lat!")
        exit()

    if szanse==0: #jeżeli szanse są równe 0
        print("Nie udało Ci się!")

##################################################################################################################

import random #zaimportuj bibliotekę zawierającą funkcję do losowania

imie=input("Jak masz na imię? ") #podaj funkcję, która pozwala pobrać coś od użytkownika
print("Cześć", imie)
wiek=int(input("Ile masz lat? ")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą

wiekKomputera=random.randint(1, 30) #podaj zakres losowania (od 1 do 30)
while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 30) #podaj zakres losowania (od 1 do 30)

if wiekKomputera>wiek #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jestem od Ciebie starszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie
else:
    print("Jestem od Ciebie młodszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat! (masz trzy szanse)"))
    if zgadywanie<wiekKomputera: #jeżeli zgadywanie jest mniejsze od wiekKomputera to
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    elif zgadywanie==wiekKomputera: #ale jeżeli zgadywanie jest równe wiekKomputera to
        print("Tak, mam tyle lat!")
        exit()
    else: #w przeciwnym razie
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    if szanse==0: #jeżeli szanse są równe 0
        print("Nie udało Ci się!")

#######################################################################################################################
import random #zaimportuj bibliotekę zawierającą funkcję do losowania

imie=input("Jak masz na imię? ") #podaj funkcję, która pozwala pobrać coś od użytkownika
print("Cześć", imie)
wiek=int(input("Ile masz lat? ")) #wpisz funkcję, która zamieni wartość wprowadzoną przez użytkownika na liczbę całkowitą

wiekKomputera=random.randint(1, 30) #podaj zakres losowania (od 1 do 30)
while wiekKomputera==wiek:
    wiekKomputera=random.randint(1, 30) #podaj zakres losowania (od 1 do 30)

if wiekKomputera>wiek #wpisz odpowiedni warunek (musi się zgadzać z tym, co wyświetla funkcja print())
    print("Jestem od Ciebie starszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie
else:
    print("Jestem od Ciebie młodszy!") #użyj funkcji pozwalającej wypisać tekst z nawiasu na ekranie

szanse=3
while szanse>0:
    zgadywanie=int(input("Zgadnij, ile mam lat! (masz trzy szanse)"))
    if zgadywanie<wiekKomputera: #jeżeli zgadywanie jest mniejsze od wiekKomputera to
        print("Mam więcej lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)
    elif zgadywanie==wiekKomputera: #ale jeżeli zgadywanie jest równe wiekKomputera to
        print("Tak, mam tyle lat!")
        exit()
    else: #w przeciwnym razie
        print("Nie mam aż tylu lat!")
        szanse-=1
        print("Liczba pozostałych szans:", szanse)

    if szanse==0: #jeżeli szanse są równe 0
        print("Nie udało Ci się!")