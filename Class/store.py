class Store:
    def __init__(self):
        self.__cart = []

    def addToCart(self, item):
        self.__cart.append(item)

    def removeFromCart(self, index):
        self.__cart.pop(index)

    def calculateTotal(self):
        total = 0
        for item in self.__cart:
            total += item.getPrice()

        return total

    def displayCart(self):
        for indx in range(0, len(self.__cart)):
            print(indx, self.__cart[indx].getName())
