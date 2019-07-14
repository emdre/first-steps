LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def get_menu_choice():
    print()
    print('Friends and their emails')
    print('------------------------------')
    print('1. Search for an email address.')
    print('2. Add an email address.')
    print('3. Change an email address.')
    print('4. Delete an email address.')
    print('5. Quit.')
    print()

    choice = int(input('Choose an option: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Choose a correct number: '))

    return choice


def look_up(emails):
    name = input('Enter the name: ')
    print(emails.get(name, 'Name not found.'))


def add(emails):
    name = input('Enter the name: ')
    mail = input('Enter the email address: ')

    if name not in emails:
        emails[name] = mail
    else:
        print('There is no such person in the file.')


def change(emails):
    name = input('Enter the name: ')

    if name in emails:
        mail = input('Enter a new email address: ')
        emails[name] = mail
    else:
        print('There is no such person in the file.')


def delete(emails):
    name = input('Enter the name: ')

    if name in emails:
        del emails[name]
    else:
        print('Person not found.')
