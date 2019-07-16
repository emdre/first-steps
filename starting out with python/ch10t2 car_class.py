class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


def main():
    car = Car(2012, 'Kia')

    for num in range(0, 5):
        car.accelerate()
        print(f"The current speed is {car.get_speed()} km/h.")

    for num in range(0, 5):
        car.brake()
        print(f"The current speed is {car.get_speed()} km/h.")


main()
