import math
figura=""

while figura!="0":
    figura=input("Podaj figurę: 1- trójkąt,2-trójkąt(inne pole), 3- prostokąt, 4-równoległobok, 5-deltoid, 6-trapez,0-błędna figura :")
    if figura=="1":
        a=float(input("Podaj długość podstawy:"))
        while a<=0:
            print("Długość podstawy nie może być mniejsza bądź równa 0.")
            a=float(input("Podaj długość podstawy:"))
        h=float(input("Podaj długość wysokości:"))
        while h<=0:
            print("Długość podstawy nie może być mniejsza bądź równa 0.")
            h=float(input("Podaj długość wysokości:"))
            pole= 0.5* a*h
        print(pole)