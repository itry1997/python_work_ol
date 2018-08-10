favourite_pleases = {
	'cuiwie': ['liaocheng','jinan'],
	'liuxuan': ['jinan','linyi','liaocheng'],
	'xijinping': ['beijing'],
	}
	
for name, pleases in favourite_pleases.items():
	print(name.title() + ": ")
	for please in pleases:
		print(please.title())
	print("\n")	
