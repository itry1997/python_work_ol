#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def get_formatted_name(first_name,last_name,middle_name = ''):
	"""返回整洁的姓名"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
while True:
	print("\nPlease tell me your name:\n")
	print("(enter 'q' at anytime to quit.)")
	
	f_name = input("First name:")
	if f_name == 'q':
		break
		
	l_name = input("Last name:")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello " + ' ' + formatted_name + '!')
