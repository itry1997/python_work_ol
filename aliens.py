#coding=utf-8
#创建一个用于储存外星人的空列表
aliens = []

#创建30个绿色外星人
for alien_number in range(30):
	new_alien = {'color': 'green','points': 5,'speed': 'slow'}
	aliens.append(new_alien)
print(alien_number)
	
#改变颜色
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

#显示前5个外星人
for alien in aliens[:5]:
	print(alien)
print("...")

#显示创建了多少外星人
print("Total number of aliens: " + str(len(aliens)))
