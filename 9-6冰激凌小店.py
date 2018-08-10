#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

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

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavours = ["apple","orange"]
		
		
my_ice = IceCreamStand("Dove","666")
my_ice.describe_restaurant()

for my_ice.flavour in my_ice.flavours:
	print(my_ice.flavour)
