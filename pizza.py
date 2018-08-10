#coding=utf-8
#储存所点披萨信息
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese'],
	}
	
#概述所点披萨
print("You ordered a " +pizza['crust'] + "-crust pizza" +
	" with the following toppings:")
for topping in pizza['toppings']:
	print("\t"+ topping)
