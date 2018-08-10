prompt = "Please enter your age.\n"
prompt += "Enter 'quit' when you finished."

while True:
	age = input(prompt)
	if age == "quit":
		break
	elif int(age) <= 3:
		print("Free")
	elif 3<int(age)<12:
		print("10 dallers")
	elif int(age)>12:
		print("15 dallers")
