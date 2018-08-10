sandwich_orders = ['name_A','name_B','name_C']
finished_sandwichs = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(current_sandwich + " ,I made your tuna sandwich")
	finished_sandwichs.append(current_sandwich)
	
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich)
	
