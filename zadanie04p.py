#wartość bezwzględną można określić jako odległość liczby od 0 na osi liczbowej
#wartość bezwzględna z liczby 5 to 5, a wartość bezwzględna z liczby -5 to 5 

liczba=int(input("Podaj liczbę całkowitą: ")) #prosimy użytkownika o podanie liczby całkowitej

if liczba>0: #jeżeli liczba jest większa od 0
    print("Wartość bezwzględna liczby", liczba, "wynosi", liczba) #napisz, że wartość bezwzględna tej liczby jest jej równa
else: #w przeciwnym razie (jeżeli wcześniejszy warunek nie został spełniony)
    wartosc_bezwgledna=liczba*(-1) #wartość bezwzględną liczby ujemnej można policzyć mnożąc ja razy -1
    print("Wartość bezwzględna liczby", liczba, "wynosi", wartosc_bezwgledna) #napisz, że wartość bezwględna jest równa zmiennej  wartosc_bezwzgledna
    print("Wartość bezwzględna tej liczby to", liczba*(-1))
    