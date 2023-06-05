# Shopping cart application 
# store / items / carts

class Item:
  def __init__(self, name, price):
    self.name = name   
    self.price = price 

cart = []

def addToCart(item):
  cart.append(item)

def removeFromCart(index):
  cart.pop(index)




