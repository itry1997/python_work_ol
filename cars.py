cars=['bmw','audi','subaru','toyota']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)
print("Here is the reverse list:")
cars.reverse()
print(cars)
print(len(cars))

print('\n')
for car in cars:
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())
