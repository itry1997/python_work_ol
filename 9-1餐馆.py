class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 110
		
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is opening.")
		
	def read_number_served(self):
		print("The restaurant has served " + str(self.number_served) + " people.")
		
	def increment_number_served(self,number):
		self.number_served += number
		
my_restaurant = Restaurant('lovecui','666')
your_restaurant = Restaurant('lovewei','777')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(666)
my_restaurant.read_number_served()



your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
