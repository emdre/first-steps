
"""
Zapisz skrypt, który, który obliczy stan konta za kilka lat. Program pyta użytkownika o: stan początkowy konta,
stopę oprocentowania rocznego (zwróć uwagę, że odsetki podlegają miesięcznej kapitalizacji)
liczbę lat na lokacie.
Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu. Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
"""



initial_balance = float(input("Podaj stan początkowy konta: "))
interest_rate = float(input("Podaj stopę oprocentowania rocznego: "))
n = int(input("Podaj liczbę lat na lokacie: "))
result = initial_balance * (1 + interest_rate * n)
print("Po {} latach na lokacie będziesz mieć {:.2f} zł".format(n, result))
