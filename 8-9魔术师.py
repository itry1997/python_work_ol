def make_great(names):
	while names:
		current_name = names.pop()
		current_name = "The Great " + current_name
		new_names.append(current_name)
		
	return new_names
	
def show_magicians(names):
	for name in names:
		print(name)
		

	
new_names = []
names = ['cuiwei','liuxuan']

new_names = make_great(names[:])
show_magicians(new_names)
show_magicians(names)
	
