class Product(object):
 	price = 0
 	count = 0
 	vat = 0

 	def price_with_vat(self):
 		return self.price * self.count * self.vat

 	def __init__(self, price, count, vat):
 		self.price = price
 		self.count = count
 		self.vat = vat

products =[Product(price=900, count=2, vat=1.25), Product(price=100, count=1, vat=1.25)]
total_price = products[0].price_with_vat() + products[1].price_with_vat()

print total_price