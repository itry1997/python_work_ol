#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def build_person(first_name,last_name,age = ''):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first': first_name,'last':last_name}
	if age:
		person['age'] = age
	
	return person
	
musician = build_person('jimi','henrix',27)
print(musician)
