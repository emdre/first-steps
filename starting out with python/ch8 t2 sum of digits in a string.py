def count_sum(user_number):
    total = 0
    for ch in user_number:
        ch = int(ch)
        total += ch
    return total


def main():
    user_number = input('Podaj ciąg cyfr nierozdzielonych żadnymi znakami: ')
    total = count_sum(user_number)
    print(f'Suma wszystkich cyfr wynosi: {total}')


main()
