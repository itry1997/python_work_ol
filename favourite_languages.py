favourite_languages = {
	'jen' : 'python',
	'sarch' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
	}
	
print("Sarch's favourite language is "+favourite_languages['sarch'].title()+".\n")

for name,language in favourite_languages.items():
	print(name.title()+ "'s favourite language is " +
	language.title() + ".")
	
print("\n================================================\n")

friends = ['jen','phil']
for name in favourite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("Hi," + name.title()+",I heard your favourite language is " +
		favourite_languages[name].title() + ".")
	elif name not in friends:
		print(name.title() + ",please take the poll.")


print("\n================================================\n")

for name in sorted(favourite_languages.keys()):
	print(name.title() + ",thank you for taking the poll.")
	
print("\n================================================\n")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())
	
print("\n")
for language in set(favourite_languages.values()):
	print(language.title())
	
