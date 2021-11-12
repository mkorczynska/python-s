def maksimum(a, b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "liczby są równe"

def minimum(a, b, c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

def nieparzysta(a):
    if a%2==0:
        return "parzysta"
    else:
        return "nieparzysta"

def unikatowe(list):
    list=set(list)
    return list

def bezwzgledna(a):
    if a>=0:
        return a
    else:
        return -a

def suma_wielu(*argumenty):
    suma = 0
    for arg in argumenty:
        suma += arg
    return suma


a=0
b=-10
c=7

list=[1,2,3,1,2,3]

print(maksimum(a, b))
print(minimum(a, b, c))
print(nieparzysta(c))
print(unikatowe(list))
print(bezwzgledna(b))
print(suma_wielu(a, b, c))