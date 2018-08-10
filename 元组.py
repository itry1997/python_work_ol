def make_pizza(size,*toppings):
	print("\nMaking a " + str(size) + "-inch pizza with following toppings:")
	for topping in toppings:
		print('- ' + topping)
	
make_pizza(16,'pepoperoni')
make_pizza(32,'mushroom','green peppers')
