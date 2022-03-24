zespoly=['YONAKA', 'Alter Bridge', 'Asking Alexandria', 'PVRIS']

print("Zespol nr 1: ",zespoly[1])

#wyswietlanie listy za pomoca petli
print("Lista zespołów:")
for i in zespoly:
    print(i)

#wyswietlanie listy z uzyciem *
print("Lista zespołów:")
print(*zespoly)

#wyswietlanie listy z uzyciem * i separatora ,
print("Lista zespołów:")
print(*zespoly, sep = ", ") 

#wyswietlanie listy z uzyciem * i separatora (nowej linii)
print("Lista zespołów:")
print(*zespoly, sep = " ")

#wyswietlanie listy z uzyciem 
print("Lista zespołów:")
print(' '.join(zespoly))