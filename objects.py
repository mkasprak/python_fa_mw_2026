"""
classes and objects

ℹ️ This file is a small "object-oriented programming" (OOP) example.
In OOP, we use:
- a *class* as a blueprint (what an object is like)
- an *object* (also called an *instance*) as a real thing made from that blueprint

"""


class Coffee:
    """
    ℹ️ A class is a blueprint for making objects.

    This Coffee class describes what data (attributes) a coffee order has and what actions
    (methods) a coffee order can do.
    """

    def __init__(self, drink_type, size, milk, flavor, price):
        # ℹ️ `__init__` is the "constructor": it runs automatically when you create a new object.
        # ℹ️ `self` is the current object being created (the instance).
        #
        # ⚠️ We use double-underscore names like `__size` to make these attributes "private-ish".
        # In Python this triggers *name mangling*, which helps prevent accidental use from outside.
        self.__drink_type = drink_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__price = price

    # ℹ️ Getters = methods that let us READ private attributes safely.

    def get_drink_type(self):
        # ✅ Return: drink type (str)
        return self.__drink_type

    def get_size(self):
        # ✅ Return: size (str)
        return self.__size

    def get_milk(self):
        # ✅ Return: milk choice (str)
        return self.__milk

    def get_flavor(self):
        # ✅ Return: flavor (str)
        return self.__flavor

    def get_price(self):
        # ✅ Return: price (str) in this example (we could also store it as a float)
        return self.__price

    # ℹ️ Setters = methods that let us CHANGE private attributes safely.
    # 💡 Tip: setters are a good place to add validation rules later (ex: only allow known sizes).

    def set_price(self, price):
        self.__price = price

    def set_drink_type(self, drink_type):
        # ⚠️ Common mistake: accidentally assign the old value back to itself.
        # We want to update the object's state using the *new* input value.
        self.__drink_type = drink_type

    def set_size(self, size):
        self.__size = size

    def set_milk(self, milk):
        self.__milk = milk

    def set_flavor(self, flavor):
        self.__flavor = flavor

    # ℹ️ Methods (functions inside a class) describe behaviors/actions an object can do.

    def return_summary(self):
        # ✅ Return: a one-line summary (str) describing this object's current state
        summary = f"Order Summary: {self.__drink_type}, {self.__size}, {self.__milk}, {self.__flavor}"

        return summary


if __name__ == "__main__":
    # ▶️ Entry point: this code runs when you execute `objects.py` directly.

    # 🧪 Create an object (an instance) from the Coffee class blueprint.
    latte = Coffee("Latte", "Large", "Whole", "Vanilla", "$ 6.00")

    # 🖨️ Call a method on the object to get information about its current state.
    print(latte.return_summary())

    # ℹ️ Mutate (change) the object by calling a setter method.
    latte.set_size("Extra Large")

    # 🖨️ The summary changed because the object's internal state changed.
    print(latte.return_summary())

    # 🖨️ Read one attribute using a getter.
    print(latte.get_drink_type())
