current_users=['admin','superman','batman','liuxuan','dr.cui']
new_names=['admin','superman','sheep','apple killer','flying bird']

for new_name in new_names:
	if new_name.lower() in current_users:
		print("This name has been used,ues another one please.")
	else:
		print("You can use this name.")
