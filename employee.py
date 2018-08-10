# -*- coding: UTF-8 -*-
class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self,raise_money = 5000):
        self.salary += raise_money
