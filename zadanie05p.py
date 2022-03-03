import random #aby móc losować wartości z przedziału musimy zaimportować bibliotekę random - znajdują się w niej funkcje losujące

szczesliwy_numerek=random.randint(1, 32) #tworzymy zmienną szczesliwy_numerek i używamy funkcji randint() z biblioteki random
#w nawiasie funkcji randint() podajemy przedział, z którego losujemy (interesują nas liczby od 1 do 32)
print("Szczęśliwy numerek to:", szczesliwy_numerek) #wypisujemy wylosowany szczęśliwy numerek
