#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def greeter_user(names):
	"""向列表中每位用户发送简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + '!'
		print(msg)
		
user_names = ['cuiwei','liuxueshu','liuxuan']
greeter_user(user_names)
