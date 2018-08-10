class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attemps = 0
		
	def describe_user(self):
		print('First name: ' + self.first_name.title())
		print('Last name: ' + self.last_name.title())
		
	def greet_user(self):
		print("Hello," + self.first_name.title() + ' ' + self.last_name.title() + '!')
		
	def increment_login_attemps(self):
		self.login_attemps += 1
		
	def reset_login_attemps(self):
		self.login_attemps = 0
	
	
user_1 = User('cui','wei')
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attemps()
user_1.increment_login_attemps()
print(str(user_1.login_attemps))

user_1.reset_login_attemps()
print(str(user_1.login_attemps))
