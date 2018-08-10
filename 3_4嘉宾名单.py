lists=['Liuxuan','David','Sherry']
message=lists[0]+','+lists[1]+' and '+lists[2]+",would you like to have dinner with me?"
print(message)
cant_come='David'
print(cant_come+" can't come.")
latest_invited="Cuiwei"
lists.remove(cant_come)
lists.append(latest_invited)
message=lists[0]+','+lists[1]+' and '+lists[2]+",would you like to have dinner with me?"
print(message)
lists.insert(0,'Xiaoming')
message=lists[0]+','+lists[1]+','+lists[2]+' and '+lists[-1]+",would you like to have dinner with me?"
print(message)
bad_news="Sorry,I can have dinner with only two people."
print(bad_news)
name_1=lists.pop()
print('Sorry '+name_1+" I can't have dinner with you.")
name_2=lists.pop()
print('Sorry '+name_2+" I can't have dinner with you.")
print(lists[0]+",you are still invited.")
print(lists[-1]+",you are still invited.")
del lists[0]
print(lists)
del lists[0]
print(lists)





