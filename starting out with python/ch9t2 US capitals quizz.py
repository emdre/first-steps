capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'Connecticut': 'Hartford', 'Dakota Pd.': 'Pierre',
            'Dakota Pn.': 'Bismarck', 'Delaware': 'Dover', 'Dystrykt Kolumbii': 'Waszyngton',
            'Floryda': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaje': 'Honolulu',
            'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kalifornia': 'Sacramento', 'Kansas': 'Topeka',
            'Karolina Pd.': 'Columbia', 'Karolina Pn.': 'Raleigh', 'Kentucky': 'Frankfort',
            'Kolorado': 'Denver', 'Luizjana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Missisipi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'Nowy Jork': 'Albany',
            'Nowy Meksyk': 'Santa Fe', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pensylwania': 'Harrisburg', 'Rhode Island': 'Providence',
            'Teksas': 'Austin', 'Tennessee': 'Nashville', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Waszyngton': 'Olympia', 'Wirginia': 'Richmond',
            'Wirginia Zach.': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenn'
            }

leave = False
correct = 0
incorrect = 0

print('Sprawdź, czy znasz wszystkie stolice stanów USA.')

while not leave and len(capitals) > 0:
    state, capital = capitals.popitem()
    print(f'Co jest stolicą stanu {state}? Aby zakończyć grę, naciśnij z.')
    guess = input('Podaj odpowiedź: ')

    if guess == capital:
        correct += 1
        print('To prawidłowa odpowiedź!')
    elif guess.lower() == 'z':
        leave = True
        print(f'Koniec gry. Liczba prawidłowych odpowiedzi to: {correct},'
              f' a liczba nieprawidłowych odpowiedzi to: {incorrect},')
    elif guess != capital:
        incorrect += 1
        print('To nie jest prawidłowa odpowiedź.')

if len(capitals) == 0:
    print(f'To już wszystkie stany. Liczba prawidłowych odpowiedzi to {correct},'
          f' a liczba nieprawidłowych odpowiedzi to: {incorrect}.')
