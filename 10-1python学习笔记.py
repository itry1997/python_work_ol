# -*- coding: UTF-8 -*-
with open('text_files/learning_python.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

with open('text_files/learning_python.txt') as file_object:
    for line in file_object:
        print(line.replace('Python','C').rstrip())

with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())