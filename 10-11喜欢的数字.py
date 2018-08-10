# -*- coding: UTF-8 -*-
import json

filename = 'favourite_number.json'

try:
    with open(filename) as f_obj:
        favourite_number = json.load(f_obj)
        print("I konw your favourite number! It's " + favourite_number)

except FileNotFoundError:
    favourite_number = input("Please enter your favourite number.")
    with open(filename, 'w') as f_obj:
        json.dump(favourite_number, f_obj)