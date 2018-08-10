# -*- coding: UTF-8 -*-
import unittest
from employee import Employee

def setUp(self):
    self.employee1 = Employee('cui','wei',6000)

def test_give_default_raise(self):
    self.employee1.give_raise()
    self.assertEqual(self.employee1.salary,11000)

if __name__ == '__main__':
    unittest
