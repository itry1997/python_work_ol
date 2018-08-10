cities = {
	'jinan': {
		'country': 'china',
		'population': '5000000',
		'fact': 'hot',
		},
		
	'newyork': {
		'country': 'ameraica',
		'population': '7500000',
		'fact': 'crowded',
		},
		
	'london': {
		'country': 'england',
		'population': '6660000',
		'fact': 'fog',
		},
	}

for city, city_info in cities.items():
	print(city.title() + ": ")
	print(city_info['country'].title())
	print(city_info['population'].title())
	print(city_info['fact'].title())
	print("\n")	
	
	
	
	
	
