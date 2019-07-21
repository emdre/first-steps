class Employee:
    def __init__(self, name, id_no):
        self.__name = name
        self.__id_no = id_no

    def set_name(self, name):
        self.__name = name

    def set_id_no(self, id_no):
        self.__id_no = id_no

    def get_name(self):
        return self.__name

    def get_id_no(self):
        return self.__id_no


class ProductionWorker(Employee):
    def __init__(self, name, id_no, shift, hourly_rate):
        Employee.__init__(self, name, id_no)
        self.__shift = shift
        self.__hourly_rate = hourly_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift(self):
        return self.__shift

    def get_hourly_rate(self):
        return self.__hourly_rate


def main():
    name = input("Enter the employee's name: ")
    id_no = input("Enter the employee's id number: ")
    shift = int(input("Enter the shift: "))
    hourly_rate = float(input("Enter the hourly rate: "))

    prod_worker1 = ProductionWorker(name, id_no, shift, hourly_rate)

    print("The employee's name is: ", prod_worker1.get_name())
    print("The employee's id number is: ", prod_worker1.get_id_no())
    print("The employee is workking on shift ", prod_worker1.get_shift())
    print("The employee's hourly rate is: ", prod_worker1.get_hourly_rate())
    print()


main()
