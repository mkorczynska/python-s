import random

liczba=random.randint(1, 50)
strzal=int(input("Zgadnij jaka to liczba całkowita: "))

while strzal!=liczba:
    if strzal<liczba:
        print("Za mało.")
        strzal=int(input("Nie zgadłeś/aś. Spróbuj jeszcze raz: "))
    elif strzal>liczba:
        print("Za dużo.")
        strzal=int(input("Nie zgadłeś/aś. Spróbuj jeszcze raz: "))
print("To ta liczba.")



