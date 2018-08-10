#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*


def discribe_pet(animal_name,animal_type = 'dog'):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + '.')
	print("My " + animal_type + "'s name is " + animal_name + '.')
	
discribe_pet(animal_type = 'hamster',animal_name = 'harry')
discribe_pet('leo')
discribe_pet(animal_name = 'Liuxuan',animal_type = 'cat')
