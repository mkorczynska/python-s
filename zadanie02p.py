#Podobnie jak w zadaniu 1 należy pobrać jakąś wartość od użytkownika
#tym razem potrzebujemy liczby
#WAŻNE - funkcja input() domyślnie zapisuje podane wartości jako tekst
#wartość wpisaną przez input() można wczytać jako liczbę za pomocą int()

wiek=int(input("Ile masz lat? ")) #w tej linijce pytamy użytkownika o wiek i zapisujemy go do zmiennej wiek
wynik=100-wiek #obliczamy, za ile lat dana osoba będzie miałą 100 lat (odejmujemy podany przez nią wiek od 100)

print("100 lat będziesz mieć za", wynik, "lat.") #za pomocą funkcji print() informujemy użytkownika za ile lat osiągnie setkę
