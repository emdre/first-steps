class Contact:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return "Name: " + self.__name +\
            "\nAdress: " + self.__address +\
            "\nAge: " + str(self.__age) +\
            "\nPhone number: " + str(self.__phone) +\
            "\n"


def main():
    contact1 = Contact('Magda', 'JŚ 15 Gdańsk', 30, 123456789)
    contact2 = Contact('Jaś', 'Zwycięstwa 200 Gdynia', 1, 987654321)
    contact3 = Contact('Łukasz', 'Morska 0 Gdynia', 31, 321654798)

    print(contact1)
    print(contact2)
    print(contact3)


main()
