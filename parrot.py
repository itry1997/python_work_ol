'''
prompt = "If you tell us who uou are,we can personalize the message you see"
prompt += "\nWhat is your first name?\n"

name = input(prompt)
print("\nHello, " + name.title() + "!")
'''

active = True
prompt = "\nTell me something,and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the problem.\n"
message = ""
while active:
	message = input(prompt)
	
	if message == "quit":
		active = False
	else:
		print(message)
