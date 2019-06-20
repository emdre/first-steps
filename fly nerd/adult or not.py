"""
Skrypt zapyta użytkownika o wiek. Jeżeli użytkownik jest przed 18 wyświetli informację „Użytkownik niepełnoletni” oraz zwróci ile lat zostało użytkownikowi do pełnoletności. Użytkownikom pełnoletnim wyświetli informację „Użytkownik pełnoletni”. Sprawdź czy wiek użytkownika nie przekracza 100 lat i wyświetl komunikat „200 lat ♫”. """

age = int(input("Ile masz lat?: "))
time_to_adulthood = 18 - age
if age <  18:
    print("Użytkownik niepełnoletni. Do osiągnięcia pełnoletności zostało lat: {}.".format(time_to_adulthood))
elif age > 100:
    print("200 lat ♫")
else:
    print("Użytkownik pełnoletni")    
    
