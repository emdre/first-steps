def main():
    alphanumeric_number = input('Enter an alphanumeric phone number formatted as XXX-XXX-XXXX:')
    letters_to_numbers = {'a': '2', 'b': '2', 'c': '2',
                          'd': '3', 'e': '3', 'f': '3',
                          'g': '4', 'h': '4', 'i': '4',
                          'j': '5', 'k': '5', 'l': '5',
                          'm': '6', 'n': '6', 'o': '6',
                          'p': '7', 'q': '7', 'r': '7', 's': '7',
                          't': '8', 'u': '9', 'v': '8',
                          'w': '9', 'x': '9', 'y': '9', 'z': '9'}

    clean_number = alphanumeric_number.replace('-', '')
    new_number = ''
    for item in clean_number:
        if item.isalpha():
            new_number += letters_to_numbers[item.lower()]
        else:
            new_number += item
    print(f'{new_number[:3]}-{new_number[3:6]}-{new_number[6:]}')


main()
