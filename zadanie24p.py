def podatek(dochod):
    if dochod<=30000:
        procent=0
        podatek=procent*dochod
        zostanie=dochod-podatek
    elif dochod<=120000:
        procent=0.17
        podatek=procent*dochod-5100
        zostanie=dochod-podatek 
    else:
        procent=0.32
        podatek=15300+(dochod-120000)*procent
        zostanie=dochod-podatek
    #return procent, podatek, zostanie
    return "Procent", procent, ". Podatek", podatek, ". Zostanie", zostanie

print(podatek(130000))