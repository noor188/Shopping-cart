# Shopping cart application 
# store / items / carts

class Item:
  def __init__(self, name, price):
    self.name = name   
    self.price = price 

class Store:
  def __init__(self):
    self.cart = []

  def addToCart(item):
    cart.append(item)

  def removeFromCart(index):
    cart.pop(index)

  def calculateTotal(cart):
    total = 0
    for item in cart:
      total += item.price
    
    return total

store = Store()
store.addToCart(Item('cup', 10))
print(store.cart)