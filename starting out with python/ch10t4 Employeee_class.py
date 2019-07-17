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
    employee1 = Employee('Sara Majweska', 47899, 'Księgowość', 'Zastępca dyrektora')
    employee2 = Employee('Marek Jankowski', 39119, 'IT', 'Programista')
    employee3 = Employee('Jan Kowlaski', 81774, 'Produkcja', 'Inżynier')

    print(employee1)
    print(employee2)
    print(employee3)


main()
