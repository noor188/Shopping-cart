# Shopping cart application
# store / items / carts

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


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
            total += item.price

        return total

    def displayCart(self):
        for indx in range(0, len(self.__cart)):
            print(indx, self.__cart[indx].name)


store = Store()
print("Welcome to our store")

while True:
    store.displayCart()
    store.calculateTotal()
    print("Press a to add item")
    print("press r to remove item")
    print("Press x to exit")

    userInput = input("Please enter a command")

    if userInput == "x":
        break
    elif userInput == "a":
        itemName = input("Please give the item a name")
        itemPrice = input("Please give the item a price")
        store.addToCart()
