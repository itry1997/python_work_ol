prompt = "\nPlease input your pizza toppings"
prompt += "\n(Enter 'quit' when you finished.)"

while True:
	toppings = input(prompt)
	
	if toppings == "quit":
		break
	else:
		print("Ok,we will have " + toppings +" in.")
