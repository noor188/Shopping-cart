# Shopping cart application
# store / items / carts
def itemName_HandleErrors():  # return itemName
    while True:
        try:
            itemName = input("Please give the item a name")
            int(itemName)
        except:  # str
            break
        else:  # number
            print('looks like you entered a number')
    return itemName


def itemPrice_HandleErrors():  # return itemPrice
    while True:
        try:
            itemPrice = float(input("Please give the item a price"))
        except:  # str
            print("looks like you didn't enter a number")
        else:  # number
            break
    return itemPrice


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


def main():
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
            itemName = itemName_HandleErrors()
            itemPrice = itemPrice_HandleErrors()
            store.addToCart(Item(itemName, itemPrice))
        elif userInput == "r":
            indx = int(
                input("Please provide the index of the item to remove it"))
            store.removeFromCart(indx)
        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()
