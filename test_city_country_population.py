# -*- coding: UTF-8 -*-
import unittest
from city_functions import get_city_country_name

class PopulationTestCase(unittest.TestCase):
    def test_city_country_population(self):
        city_country_population = get_city_country_name('santiago','china','5000000')
        self.assertEqual(city_country_population,'santiago,china-population 5000000')

if __name__ == '__main__':
    unittest