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
