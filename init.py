class Product(object):
 	price = 0
 	count = 0
 	vat = 0

 	def __init__(self, price, count, vat):
 		self.price = price
 		self.count = count
 		self.vat = vat

robot = Product(price =900, count =2, vat =1.25)
book = Product(price = 100, count = 1, vat = 1.06)

print __init__ 