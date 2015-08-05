class Product(object):
 	price = 0
 	count = 0
 	vat = 0

 	def price_with_vat(self):
 		return self.price * self.count * self.vat
 		if self.price > 500:
 			return 0.9 * total
 		else: 
 			return total

 	def __init__(self, price, count, vat):
 		self.price = price
 		self.count = count
 		self.vat = vat


products =[Product(price=900, count=2, vat=1.25), Product(price=100, count=1, vat=1.06)]
total_price = 0

for product in products:
	#print product.price_with_vat()
	total_price += product.price_with_vat()

print total_price