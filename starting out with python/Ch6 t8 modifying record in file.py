import os
def main():
    found = False
    search = input('Enter the name of the student whose result you want to edit: ')
    new_result = float(input('Enter the new result: '))
    student_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    name = student_file.readline()
    while name != '':
        result = float(student_file.readline())
        name = name.rstrip('\n')
        if name == search:
            temp_file.write(name + '\n')
            temp_file.write(str(new_result) + '\n')
            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(str(result) + '\n')
        name = coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')
    if found:
        print('The file was updated.')
    else:
        print('The name was not found.')
main()    
