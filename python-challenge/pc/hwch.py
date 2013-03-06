'''
Created on 04.03.2013

@author: Vladimir
'''

import random

s = -2107343835 # hello
s = -2138154165 # world

random.seed(s)

for i in range(5):
    print chr(96 + random.randint(0, 26)),