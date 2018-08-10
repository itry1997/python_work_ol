# -- coding: utf-8 --

responses = {}

#设置一个标志，判断循环是否继续
polling_active = True

while polling_active:
	#提示输入被调查者的名字和回答
	name = input("\nWhat's your name?")
	response = input("\nWhich mountain would you like to clib someday?")
	
	#将答案储存在字典中
	responses[name] = response
	
	#看看是否还有人要参加调查
	repeat = input("\nWould you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
		
#调查结束，显示结果
print("\n---Poll Results---")
for name , response in responses.items():
	print(name + " would like to climb " + response + '.')




