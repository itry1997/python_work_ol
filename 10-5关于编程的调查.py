# -*- coding: UTF-8 -*-
filename = 'reasons.txt'

reason = input("Why do you love Python?\n")
while reason != 'q':
    with open(filename,'a') as file_object:
        file_object.write(reason + "\n")
    reason = input()
