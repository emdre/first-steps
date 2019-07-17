import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


FILENAME = 'employees.dat'


class Employee:
    def __init__(self, name, id_no, department, job_title):
        self.__name = name
        self.__id_no = id_no
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_no(self, id_no):
        self.__id_no = id_no

    def set_age(self, department):
        self.__department = department

    def set_phone(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_no(self):
        return self.__id_no

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return "Name: " + self.__name +\
            "\nId no.: " + str(self.__id_no) +\
            "\nDepartment: " + self.__department +\
            "\nJob title: " + self.__job_title +\
            "\n"


def main():

    employees = load_employees()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    save_employees(employees)


def load_employees():

    try:
        input_file = open(FILENAME, 'rb')
        employees_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        employees_dct = {}

    return employees_dct


def get_menu_choice():
    print()
    print('Menu')
    print('------------------------------')
    print('1. Look up an employee.')
    print('2. Add a new employee.')
    print('3. Change an employee.')
    print('4. Delete an employee.')
    print('5. Quit app.')
    print()

    choice = int(input('Choose an option: '))

    while choice < LOOK_UP or choice > QUIT:
        print(input('Enter a correct value: '))

    return choice


def look_up(employees):
    id_no = int(input("Enter the employee's id number: "))

    print(employees.get(id_no, 'Person not found.'))


def add(employees):
    name = input("Enter the employee's name: ")
    id_no = int(input("Enter the employee's id number: "))
    department = input("Enter the epmloyee's department: ")
    job_title = input("Enter the employee's job title: ")

    entry = Employee(name, id_no, department, job_title)

    if id_no not in employees:
        employees[id_no] = entry
        print("Employee added.")
    else:
        print("Employee is already in the database.")


def change(employees):
    id_no = int(input("Enter the employee's id number: "))

    if id_no in employees:
        name = input("Enter the employee's name: ")
        department = input("Enter the epmloyee's department: ")
        job_title = input("Enter the employee's job title: ")

        entry = Employee(name, id_no, department, job_title)

        employees[id_no] = entry
        print("Data has been saved.")
    else:
        print("Person not found.")


def delete(employees):
    id_no = int(input("Enter the employee's id number: "))

    if id_no in employees:
        del employees[id_no]
        print("Employee deleted.")
    else:
        print("Person not found.")


def save_employees(employees):
    output_file = open(FILENAME, 'wb')

    pickle.dump(employees, output_file)

    output_file.close()


main()
