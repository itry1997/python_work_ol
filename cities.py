prompt = "\nPlease enter the name of a city of you visited:"
prompt += "\n(Enter 'quit' when you finished.)"

while True:
	city = input(prompt)
	
	if city == "quit":
		break
		
	else:
		print("I'd love to go to " + city.title() + "!")
