a=float(input("Podaj długość pierwszgo boku trójkąta: "))
b=float(input("Podaj długość drugiego boku trójkąta: "))
c=float(input("Podaj długość trzeciego boku trójkąta: "))

if a+b>c and a+c>b and b+c>a:
    print(f"Z boków {a}, {b}, {c} można zbudować trójkąt.")
else:
    print(f"Z podanych boków nie można zbudować trójkąta.")