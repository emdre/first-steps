class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    name = input('Enter the name of your pet: ')
    animal_type = input('Enter the species: ')
    age = float(input("Enter your pet's age in years: "))

    animal = Pet(name, animal_type, age)

    print('Here is the data you entered: ')
    print("Your pet's name is: ", animal.get_name())
    print("Your pet is a: ", animal.get_type())
    print("Your pet is", animal.get_age(), "year(s) old.")
    print()


main()
