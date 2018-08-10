# -*- coding: UTF-8 -*-
with open('text_files/pi_digits.txt') as file_object:
    lines = file_object.readlines()

#for line in lines:
#    print(line.rstrip())
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))