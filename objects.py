"""
classes and objects

"""


class Coffee:
    def __init__(self, drink_type, size, milk, flavor, price):
        self.__drink_type = drink_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__price = price

    #  Getters

    def get_drink_type(self):
        return self.__drink_type

    def get_size(self):
        return self.__size

    def get_milk(self):
        return self.__milk

    def get_flavor(self):
        return self.__flavor

    def get_price(self):
        return self.__price

    #  Setters

    def set_price(self, price):
        self.__price = price

    def set_drink_type(self, drink_type):
        self.__drink_type = self.__drink_type

    def set_size(self, size):
        self.__size = size

    def set_milk(self, milk):
        self.__milk = milk

    def set_flavor(self, flavor):
        self.__flavor = flavor

    # object summary

    def return_summary(self):
        summary = f"Order Summary: {self.__drink_type}, {self.__size}, {self.__milk}, {self.__flavor}"

        return summary


latte = Coffee("Latte", "Large", "Whole", "Vanilla", "$ 6.00")

print(latte.return_summary())

latte.set_size("Extra Large")

print(latte.return_summary())

print(latte.get_drink_type())
