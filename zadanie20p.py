czy_sumowac="tak"
suma=0
while czy_sumowac=="tak":
    liczba=int(input("Podaj liczbę: "))
    suma=suma+liczba
    czy_sumowac=input("Czy sumować dalej? ")
print(suma)

############################################
""" czy_sumowac = "tak"
suma = 0
while czy_sumowac == "tak" or czy_sumowac == "Tak":
    liczba = int(input("Podaj liczbę: "))
    suma = suma+liczba
    czy_sumowac = input("Czy sumować dalej? ")
if czy_sumowac == "nie":
    print("Ok, dzięki. ")
elif czy_sumowac == "nie wiem":
    print("Niezdecydowany użytkownik.")
else:
    print("Nie rozumiem. Koniec programu.")

print("Suma podanych przez Ciebie liczb to:", suma)
 """