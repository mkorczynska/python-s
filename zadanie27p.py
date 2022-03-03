slownik={  
    "dom": "house",
    "kot": "cat",
    "pies": "dog" 
}

slowo=input("Podaj slowo: ")
slowo=str.lower(slowo)

if slowo in slownik:
    print(slownik[slowo])
else:
    print("Brak słowa w słowniku.")