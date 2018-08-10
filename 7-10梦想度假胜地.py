responses = {}

user_active = True

while user_active:
	name = input("\nWhat's your name?\n")
	place = input("\nIf you could visit one place in the world,where would you go?\n")
	
	responses[name] = place
	
	repeat = input("\nIf somebady else want to join us?\n")
	if(repeat == 'no'):
		user_active = False
		
for name,place in responses.items():
	print(name.title() + " would visit " + place.title() + '.')
