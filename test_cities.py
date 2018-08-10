# -*- coding: UTF-8 -*-
import unittest
from city_functions import get_city_country_name

class CityTestCase(unittest.TestCase):
    def test_city_functions(self):
        city_country_name = get_city_country_name('santiago','chile')
        self.assertEqual(city_country_name,'santiago,chile')

if __name__ == '__main__':
    unittest