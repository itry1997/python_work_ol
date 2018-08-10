# -*- coding: UTF-8 -*-
from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarch'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name,language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
          language.title() + '.')