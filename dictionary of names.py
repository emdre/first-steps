"""Utwórz zbiór imion męskich i żeńskich. Poproś użytkownika o podanie imienia. Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację. Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.” Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. Dodaj imię do listy."""

male_female_names = {
    "Magdalena": "żeńskie",
    "Łukasz": "męskie",
    "Jan": "męskie",
    "Alicja": "żeńskie",
    "Aleksandra": "żeńskie",
    "Mateusz": "męskie",
    "Katarzyna": "żeńskie"
    }
name = input("Wpisz imię: ")

if name in list(male_female_names.keys()):
    print("{} to imię {}.".format(name, male_female_names[name]))
else:
    print("Nie znamy tego imienia. Dodaj je do listy.")
    gender = input("To imię męskie czy żeńskie? Wpisz m/z: ")
    if gender == "m":
        male_female_names[name] = "męskie"
    else:
        male_female_names[name] = "żeńskie"
    print(list(male_female_names.keys()))    

    
    
