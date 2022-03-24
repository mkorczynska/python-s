import random

losowanie = []
strzaly=[]

for i in range(6):
    a=random.randint(1, 50)
    losowanie.append(a)
    b=int(input(f"Podaj liczbę {i+1 } z 6: "))
    while b>50 or b<1:
        print("Podaj liczbę z zakresu od 1 do 50.")
        b=int(input(f"Podaj liczbę {i+1} z 6: "))
    strzaly.append(b)
    
print("Wylosowane liczby: ")
print(*losowanie, sep=', ')
print("Twoje liczby: ")
print(*strzaly, sep=', ')

trafione=set(losowanie)&set(strzaly)

if len(trafione)>0:
    print(f"Trafiłeś {len(trafione)} z 6 liczb. Oto one: {trafione}")
else:
    print("Nie trafiłeś żadnej z liczb.")

random.choice() 

