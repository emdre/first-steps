def main():
    name = input('Podaj swoje imię i nazwisko:')
    for item in name.split():
        print(f'{item[0].upper()}. ', end='')
main()