def sandwich(*toppings):
	print("Folowing toppings have been taken:")
	for topping in toppings:
		print('- ' + topping)
		
sandwich('mushroom')
sandwich('apple','extra cheese')

