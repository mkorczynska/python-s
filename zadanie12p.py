ile_wielokrotnosci=int(input("Ile chcesz wielokrotności?"))

for i in range(ile_wielokrotnosci):
    print((i+1)*10)

for i in range(10, ile_wielokrotnosci*10+1, 10):
    print(i)