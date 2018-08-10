names=['CuiWei','admin','LiuXuan','David','Jake','John']
if names:
	for name in names:
		if name == 'admin':
			print("Hello admin,would you like to see a status reports?")
		else:
			print("Hello "+name+",thank you for log in again.")
else:
	print("We need users.")
