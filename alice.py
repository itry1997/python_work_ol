# -*- coding: UTF-8 -*-
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + filename + " dose not exit."
    print(msg)
