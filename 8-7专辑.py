def make_album(name,album):
	musician = {'name':name,'album':album}
	return musician

while True:
	print("\nPlease input the name and the album.")
	print("(enter 'q' at any time to quit.)")
	name = input("Name:")
	if name == 'q':
		break
	album = input("Album:")
	if album == 'q':
		break
	musician = make_album(name,album)
	print(musician)
	
