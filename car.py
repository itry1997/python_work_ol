#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		"""初始化汽车属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometre_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()
		
	def read_odometre(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometre_reading) + " miles on it.")
		 
	def update_odometre(self,mileage):
		"""
		将里程表设置成指定的值
		禁止将里程表指数往回调
		"""
		if mileage >= self.odometre_reading:
			self.odometre_reading = mileage
		else:
			print("You can't roll back an odometre!")	 
		 
	def increment_odometre(self,miles):
		"""将里程表数增加指定的量"""
		self.odometre_reading += miles	 
	
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometre(23500)
my_new_car.read_odometre()

my_new_car.increment_odometre(100)
my_new_car.read_odometre()

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	
	def __init__(self,battery_size = 70):
		"""初始化电瓶属性"""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""打印一条描述电瓶容量的信息"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 275
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		self.battery_size = 85
	
	
class ElectricCar(Car):
	"""
	电动汽车的独特之处
	初始化父类属性，再初始化电动汽车特有属性
	"""
	
	def __init__(self,make,model,year):
		"""初始化父类属性"""
		super().__init__(make,model,year)
		self.battery = Battery()
		
	def describe_battery(self):
		"""打印一条描述电瓶容量的信息"""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
		
	def fill_gas_tank(self):
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")
	

	
	
	
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

