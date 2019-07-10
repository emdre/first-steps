import os


def main():
    found = False
    search = input('Enter the name of the student to be removed from the list: ')
    students_file = open('students.txt', 'r')
    temp_file = open('tempt.txt', 'w')
    name = students_file.readline()
    while name != '':
        result = float(students_file.readline())
        name = name.rstrip('\n')
        if name != search:
            temp_file.write(name + '\n')
            temp_file.write(str(result) + '\n')
        else:
            found = True
        name = students_file.close()
        temp_file.close()
        os.remove('students_file.txt')
        os.rename('temp.txt', 'students_file.txt')
        if found:
            print('The file was updated.')
        else:
            print('Name not found.')


main()
