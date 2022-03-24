czy_sumowac="tak"
suma=0
while czy_sumowac=="tak":
    liczba=int(input("Podaj liczbę: "))
    suma=suma+liczba
    czy_sumowac=input("Czy sumować dalej? ")
print(suma)

