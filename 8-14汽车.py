def make_car(home,kind,**other_info):
	car = {}
	car['home'] = home
	car['kind'] = kind
	
	for key,value in other_info.items():
		car[key] = value
		
	return car
	
car = make_car('subaru','outback',
			   color = 'blue',
			   tow_package = 'Ture',)
			   
print(car)
