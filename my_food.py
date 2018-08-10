my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]


my_food.append('cannoli')
friend_food.append('ice cream')
print("My favourite foods are:")
#print(my_food)
for food in my_food:
	print(food)


print("\nMy friend's favourite food are:")
#print(friend_food)
for food in friend_food:
	print(food)
