import random
for i in range(1, 51):
    if i%2==0:
        print(f"liczba {i} jest parzysta")
        #print("Liczba", i, "jest parzysta.")
    else:
        print(f"liczba {i} jest nieparzysta")
        #print("Liczba", i, "jest nieparzysta.")


for i in range(10):
    los=random.randint(1,100)
    if los%2==0:
        print(f"liczba {los} jest parzysta")
        #print("Liczba", i, "jest parzysta.")
    else:
        print(f"liczba {los} jest nieparzysta")
        #print("Liczba", i, "jest nieparzysta.")