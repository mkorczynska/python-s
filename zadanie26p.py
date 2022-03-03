import random

imiona=["Ada", "Adam", "Arek", "Ewa", "Anna"]

 
def los(lista):
    for i in lista:
        print(i," - ", random.randint(1, 200))

los(imiona)