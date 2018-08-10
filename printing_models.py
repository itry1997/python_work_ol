#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def print_models(unprinted_designs,completed_models):
	"""
	模拟每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移动到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#模拟过程
		print("Printing model:" + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	"""显示好打印好的模型"""
	print("\nFolowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
		
unprinted_designs = ['iphone','cake','cat']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)	
	
	
	
	
	
