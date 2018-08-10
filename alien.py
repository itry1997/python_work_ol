# -- coding: utf-8 --
alien_0 = {'color':'green','point':5}

new_points = alien_0['point']
print("You just earned "+str(new_points)+" points.")

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

print("\nThe alien is "+alien_0['color']+".")
alien_0['color'] = 'yellow'
print("The alien now is "+alien_0['color']+'.')

print("\n___________________________________________________")
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position: "+str(alien_0['x_position']))
#向右移动外星人
#根据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
	
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("Now x-position: "+str(alien_0['x_position']))

del alien_0['y_position']
print(alien_0)
