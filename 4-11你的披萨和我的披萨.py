my_pizzas=['New York style','Chicago style','Thick style']
friend_pizzas=my_pizzas[:]
my_pizzas.append('Cracker and Thin style')
friend_pizzas.append('stufffed')
print(my_pizzas)
print(friend_pizzas)

print("\nMy favourite pizzas are:")
for my_pizza in my_pizzas:
	print(my_pizza)

print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
