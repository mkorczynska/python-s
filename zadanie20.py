#iteracyjnie
ile_liczb=int(input("Ile wyrazów ciągu Fibonacciego wypisać?"))

a=0
b=0
ciag=[0,1]
for i in range(ile_liczb-2):
        ciag.append(ciag[i] + ciag[(i + 1)])

print(*ciag)