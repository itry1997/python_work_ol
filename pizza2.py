#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size) + "-inch pizza with following toppings:")
	for topping in toppings:
		print("-" + topping)
