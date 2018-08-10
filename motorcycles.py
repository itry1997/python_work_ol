motorcycles=["honda","yamaha","suzuki"]
print(motorcycles)
motorcycles[0]="ducati"
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
#motorcycles.insert(-1,'Mazha')
#print(motorcycles)
#del motorcycles[-1]
#print(motorcycles)
#poped_motorcycles=motorcycles.pop(2)
#print(motorcycles)
#print(poped_motorcycles)
too_expensive="ducati"	
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is to expensive for me.')
