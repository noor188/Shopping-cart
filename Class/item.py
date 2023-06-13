class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price
