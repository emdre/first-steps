def main():
    rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    teacher = {'CS101': 'Huzar', 'CS102': 'Abramowski', 'CS103': 'Romanowski', 'NT110': 'Blady', 'CM241': 'Lewandowski'}
    time = {'CS101': '8.00', 'CS102': '9.00', 'CS103': '10.00', 'NT110': '11.00', 'CM241': '13.00'}
    course = input('Podaj nr kursu: ')
    if course in rooms or teacher or time:
        print(f'Oto informacje o kursie {course}:' + '\n' + f'Sala: {rooms[course]}'
              + '\n' + f'Instruktor: {teacher[course]}' '\n' + f'Godzina rozpoczęcia: {time[course]}')
    else:
        print('Taki kurs nie istnieje. Podaj prawidłowy nr kursu: ')


main()
