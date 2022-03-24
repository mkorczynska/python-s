import random
  
znaki=["kamień", "papier", "nożyce"]

punkty_k=0
punkty_g=0

while punkty_g<3 and punkty_k<3:
    komputer=random.choice(znaki)
    gracz=input("kamień, papier czy nożyce? ")
    if gracz==komputer:
        print("remis")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="kamień" and komputer=="nożyce":
        punkty_g+=1
        print("Punkt dla gracza")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="kamień" and komputer=="papier":
        punkty_k+=1
        print("Punkt dla komputera")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="papier" and komputer=="nożyce":
        punkty_k+=1
        print("Punkt dla komputera")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="papier" and komputer=="kamień":
        punkty_g+=1
        print("Punkt dla gracza")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="nożyce" and komputer=="kamień":
        punkty_k+=1
        print("Punkt dla komputera")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")
    elif gracz=="nożyce" and komputer=="papier":
        punkty_g+=1
        print("Punkt dla gracza")
        print(f"Gracz - {punkty_g}, komputer - {punkty_k}")  
    else:
        print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
