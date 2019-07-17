class Patient:
    def __init__(self, name, address, phone, contact_person):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__contact_person = contact_person

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_contact_person(self, contact_person):
        self.__contact_person = contact_person

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_contact_person(self):
        return self.__contact_person

    def __str__(self):
        return "Name: " + self.__name + \
            "\nAddress: " + self.__address + \
            "\nPhone number: " + self.__phone + \
            "\nContact person: " + self.__contact_person + \
            "\n"


class Procedure:
    def __init__(self, name, date, physician, charge):
        self.__name = name
        self.__date = date
        self.__physician = physician
        self.__charge = charge

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_physician(self, physician):
        self.__physician = physician

    def set_charge(self, charge):
        self.__charge = charge

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_physician(self):
        return self.__physician

    def get_charge(self):
        return self.__charge

    def __str__(self):
        return "Name of the procedure: " + self.__name + \
               "\nDate: " + str(self.__date) + \
               "\nPysician: " + self.__physician + \
               "\nCharge: " + format(self.__charge, '.2f') + \
               "\n"


def main():
    patient = Patient('Jan Kowalski', 'Ulica Sezamkowa 10, 10-000 Sezamowo', '123456789', 'Janina Kowalska, 987654321')
    procedure1 = Procedure('physical examination', 'today', 'Ignaczak, MD', 250.00)
    procedure2 = Procedure('X-ray', 'today', 'Jóźwiak, MD', 500.00)
    procedure3 = Procedure('blood test', 'today', 'Styczuk, MD', 200.00)

    total_cost = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()

    print(patient)
    print(procedure1)
    print(procedure2)
    print(procedure3)

    print('Total charge for the procedures is ' + format(total_cost, '.2f') + ' PLN.')


main()
