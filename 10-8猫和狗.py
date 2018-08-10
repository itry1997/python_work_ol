# -*- coding: UTF-8 -*-
filename1 = "cats.txt"
filename2 = "dogs.txt"
filename3 = "superman.txt"

try:
    with open(filename3) as f_obj1:
        for line in f_obj1:
            print(line.rstrip().title())
except FileNotFoundError:
    #print("Sorry,can't find the file.")
    pass