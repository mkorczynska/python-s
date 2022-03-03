figura=''

while figura!='0':
    figura=input("Podaj figurę (1-trojkat, 2-prostokat, 3-rownoleglobok, 4-deltoid, 5-trapez, 0-koniec): ")
    if figura=="1":
        a=float(input("Podaj dlugosc podstawy: "))
        while a<=0:
            print("Długość podstawy trójkąta nie może być mniejsza lub równa 0.")
            a=float(input("Podaj dlugosc podstawy jeszcze raz: "))
        h=float(input("Podaj dlugosc wysokosci: "))
        while h<=0:
            print("Długość wysokości trójkąta nie może być mniejsza lub równa 0.")
            h=float(input("Podaj długość wysokości jeszcze raz: "))
        pole=0.5*a*h
        print(pole)
    elif figura=="2":
        a=float(input("Podaj długość pierwszego boku: "))
        b=float(input("Podaj długość drugiego boku: "))
        while a<=0 or b<=0:
            print("Długości boków prostokąta nie mogą być mniejsze lub równe 0.")
            a=float(input("Podaj długość pierwszego boku jeszcze raz: "))
            b=float(input("Podaj długość drugiego boku jeszcze raz: "))
        pole=a*b
        print(pole)
    elif figura=="3":
        a=float(input("Podaj długość podstawy: "))
        h=float(input("Podaj dlugosc wysokosci: "))
        while a<=0 or h<=0:
            if a<=0:
                print("Długość podstawy równoległoboku nie może być mniejsza lub równa 0.")
                a=float(input("Podaj długość podstawy jeszcze raz: "))
            elif h<=0:
                print("Długość wysokości równoległoboku nie może być mniejsza lub równa 0.")
                h=float(input("Podaj długość wysokości jeszcze raz: "))
        pole=a*h
        print(pole)
    elif figura=="4":
        da=float(input("Podaj długość pierwszej przekątnej: "))
        db=float(input("Podaj długość drugiej przekątnej: "))
        while da<=0 or db<=0:
            if da<=0:
                print("Długość pierwszej przekątnej deltoidu nie może być mniejsza lub równa 0.")
                da=float(input("Podaj długość przekątnej jeszcze raz: "))
            elif db<=0:
                print("Długość drugiej przekątnej deltoidu nie może być mniejsza lub równa 0.")
                db=float(input("Podaj długość przekątnej jeszcze raz: "))
        pole=0.5*da*db
        print(pole)
    elif figura=="5":
        a=float(input("Podaj długość dolnej podstawy: "))
        b=float(input("Podaj długość górnej podstawy: "))
        h=float(input("Podaj długość wysokości: "))
        while a<=0 or b<=0 or h<=0:
            if a<=0:
                print("Długość dolnej podstawy trapezu nie może być mniejsza lub równa 0.")
                a=float(input("Podaj długość podstawy jeszcze raz: "))
            elif b<=0:
                print("Długość górnej podstawy trapezu nie może być mniejsza lub równa 0.")
                b=float(input("Podaj długość podstawy jeszcze raz: "))
            elif h<=0:
                print("Długość wysokości trapezu nie może być mniejsza lub równa 0.")
                h=float(input("Podaj długość wysokości jeszcze raz: "))
        pole=0.5*(a+b)*h
        print(pole)
    else:
        if figura!="0":
            print("Błędny znak.")
print("Dzięki za skorzystanie z kalkulatora pól.")