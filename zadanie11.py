x=int(input("Podaj współrzędną x: "))
y=int(input("Podaj współrzędną y: "))

if x>0:
    if y>0:
        print("I")
    else:
        print("IV")
else:
    if y>0:
        print("II")
    else:
        print("III")