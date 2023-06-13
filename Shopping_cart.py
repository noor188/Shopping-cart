# Shopping cart application
# store / items / carts
from Class import item
from Class import store
from Errors import Input_Errors


def main():
    myStore = store.Store()
    print("** Welcome to our store **")

    while True:
        myStore.displayCart()
        myStore.calculateTotal()
        print("Press a to add item")
        print("press r to remove item")
        print("Press x to exit")

        userInput = input("Please enter a command")

        if userInput == "x":
            break
        elif userInput == "a":
            itemName = Input_Errors.itemName_HandleErrors()
            itemPrice = Input_Errors.itemPrice_HandleErrors()
            myStore.addToCart(item.Item(itemName, itemPrice))
        elif userInput == "r":
            indx = int(
                input("Please provide the index of the item to remove it"))
            myStore.removeFromCart(indx)
        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()
