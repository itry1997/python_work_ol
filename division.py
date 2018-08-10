# -*- coding: UTF-8 -*-
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
"""
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number)/int(second_number)
    except:
        print("You can't divide by 0.")
    else:
        print(str(answer))