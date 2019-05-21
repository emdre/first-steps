"""Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć.
W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
Dodaj serial do spisu."""

shows = {"Game of Thrones": 9, "Stranger Things": 8, "Dark": 9, "Big Little Lies": 10}
print(list(shows.keys()))
name = input("Jaki serial chcesz obejrzeć? ")
print("Serial {} otrzymał ocenę {}".format(name, shows[name]))

new = input("Jaki serial chcesz dodać do bazy? ")
new_rating = input("Podaj jego ocenę: ")
shows[new] = float(new_rating)
print(list(shows.keys()))
