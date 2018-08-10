liuxuan = {
	'first_name' : 'xuan',
	'last_name' : 'liu',
	'age' : 18,
	'city' : 'linyi',
	}
	
cuiwei = {
	'first_name': 'wei',
	'last_name': 'cui',
	'age': 19,
	'city': 'liaocheng',
	}
	
xijinping = {
	'first_name': 'jinping',
	'last_name': 'xi',
	'age': '58',
	'city': 'beijing',
	}
	
peoples = [liuxuan,cuiwei,xijinping]
	
for people in peoples:
	full_name = people['first_name'] + ' ' + people['last_name']
	
	print("Full name: " + full_name.title())
	print("Age: " + str(people['age']))
	print("City: " + people['city'].title())
	
'''
print("Her first name is " + liuxuan['first_name'].title()+
	" and her last name is " + liuxuan['last_name'].title()+
	".\nHer age is " + liuxuan['age'] + 
	".\nNow she live in " + liuxuan['city'].title()+".")

'''
