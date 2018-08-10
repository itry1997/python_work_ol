# -*- coding: UTF-8 -*-
filename = 'guest_name.txt'


name = input("Please input your name.(quit with input 'q')\n")
while name != 'q':
    with open(filename,'a') as file_object:
        file_object.write(name + "\n")
    name = input("Please input your name.(quit with input 'q')\n")