"""Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55"""

total = 0             
for digit in range(1, 11):
    total = total + digit
    print(total)

    
