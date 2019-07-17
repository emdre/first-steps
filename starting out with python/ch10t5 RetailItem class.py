class RetailItem:
    def __init__(self, description, in_stock, price):
        self.__description = description
        self.__in_stock = in_stock
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_in_stock(self, in_stock):
        self.__in_stock = in_stock

    def set_price(self, price):
        self.__price = price

    def get_decription(self):
        return self.__description

    def get_in_stock(self):
        return self.__in_stock

    def get_price(self):
        return self.__price

    def __str__(self):
        return "Description: " + self.__description + \
               "\nId no.: " + str(self.__in_stock) + \
               "\nPrice: " + str(self.__price) + \
               "\n"


def main():
    item1 = RetailItem('Marynarka', 12, 59.95)
    item2 = RetailItem('Dżinsy', 40, 34.95)
    item3 = RetailItem('Podkoszulek', 20, 24.95)

    print(item1)
    print(item2)
    print(item3)


main()
