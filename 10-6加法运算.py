# -*- coding: UTF-8 -*-
print("Give me two numbers,and I'll sum them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can only enter numbers.")
    else:
        print(str(answer))