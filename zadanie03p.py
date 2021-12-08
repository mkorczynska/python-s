#należy poprosić użytkownika o podanie liczby
#instrukcja warunkowa IF..ELIF..ELSE pozwala sprawdzać czy podane warunki są spełnione
#jako pierwsze zawsze podajemy if, a następnie warunek, który sprawdzamy
#na końcu linii stawiamy dwukropek
#bardzo ważne są wcięcia w kodzie - wszystkie instrukcje po dwukropku mają wcięcie
#słowa if, elif, else muszą znajdować się w jednej linii (nie mają wcięć)
#w przypadku if i elif należy podać warunek, który chcemy sprawdzić
#przy else nie podajemy warunku - else mówi, co ma się stać, jeżeli żaden z wcześniejszych warunków nie został spełniony

liczba=int(input("Podaj liczbę całkowitą: ")) #prosimy użytkownika o podanie liczby całkowitej i zapisujemy ją do zmiennej liczba

if liczba>0: #jeżeli liczba jest większa od 0
    print("Liczba", liczba, "jest dodatnia.") #napisz, że liczba jest dodatnia
elif liczba==0: #jeżeli liczba jest równa 0
    print("Liczba", liczba, "jest równa zero") #napisz, że liczba jest równa zero
else: #w przeciwnym razie (jeżeli żaden z wcześniejszych warunków nie jest spełniony)
    print("Liczba ", liczba, "jest ujemna.") #napisz, że liczba jest ujemna

if liczba%2==0: #jeżeli reszta z dzielenia liczby przez 2 jest równa 0
    print("Liczba", liczba, "jest podzielna przez 2.") #napisz, że liczba jest podzielna przez 2
else: #w przeciwnym razie (jeżeli wcześniejszy warunek nie jest spełniony)
    print("Liczba", liczba, "nie jest podzielna przez 2.") #napisz, że liczba nie jest podzielna przez 2
