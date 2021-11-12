import random

losowanie = []
strzaly=[]

for i in range(6):
    a=random.randint(1, 50)
    losowanie.append(a)
    b=input(f"Podaj liczbę {i+1} z 6: ")
    b=int(b)
    strzaly.append(b)

print(*losowanie, sep=', ')
print(*strzaly, sep=', ')

trafione=set(losowanie)&set(strzaly)

print(f"Trafiłeś {len(trafione)} z 6 liczb. Oto one: {trafione}")

