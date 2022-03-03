............. #zaimportuj bibliotekę zawierającą funkcje losujące

wiek=..................... #użyj funkcji losującej liczby całkowite z przedziału od 10 do 50
print("Cześć, jestem kalkulator Edward. Mam "...... "lat.") #uzupełnij kod w taki sposób, by w odopowiednim miejscu wyświetlał wartość zmiennej wiek

decyzja="0"
 
while decyzja!="9":
    decyzja=.....("Chcesz wykonać działanie? (TAK - wybierz 1/NIE - wybierz 9): ")
    #do linii 9 - #podaj funkcję, która pozwala pobrać coś od użytkownika
    if decyzja=="1":
        dzialanie=int(input("Jakie działanie chcesz wykonać? 3 - dodawanie, 4 - dzielenie, 5 - wartość bezwzględna"))
        ................ #jeżeli zmienna dzialanie jest równa 3 to
            liczba1=int(input("Podaj pierwszy składnik sumy: "))
            liczba2=int(input("Podaj drugi składnik sumy: "))
            suma=liczba1+liczba2
            print("Wynik tego dodawania to:", suma)
        .................. #ale jeżeli zmienna dzialanie jest równa 4
            liczba1=int(input("Podaj dzielną: "))
            liczba2=int(input("Podaj dzielnik: "))
            while liczba2==0:
                liczba2=int(input("Nie można dzielić przez 0. Podaj dzielnik jeszcze raz: "))
            iloczyn=liczba1*liczba2
        .................. #ale jeżeli zmienna dzialanie jest równa 5 to
            liczba=int(input("Podaj liczbę całkowitą: "))
            ............. #jeżeli liczba jest większa lub równa od 0 to
                wb=liczba
            else:
                wb=......... #wpisz prawidłowe działanie, które pozwala obliczyć wartość bezwzględną, jeżeli warunek z if nie jest spełniony
        ..... #w przeciwnym razie
            print("Zły znak")
print("Dzięki za skorzystanie z kalkulatora!")