"""Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony"""

cnt = int(input("Podaj liczbę: "))
for i in range(0, cnt):
    if cnt % 3 == 0:
        print("Podana liczba jest wielokrotnością cyfry 3.")
        if cnt % 4 == 0:
            print("Podana liczba jest wielokrotnością cyfry 4.")
            if cnt % 4 == 0 and cnt % 3 == 0:
                print("Hurra")
    else:
        print("*")
        
