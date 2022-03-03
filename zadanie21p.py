liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

if liczba1>0 and liczba2>0:
    print("Obie liczby są większe od 0.")
elif liczba1<0 and liczba2<0:
    print("Obie liczby są mniejsze od 0")
elif liczba1==0 and liczba2==0:
    print("Obie liczby są równe 0.")
else:
    print("liczby są różne")