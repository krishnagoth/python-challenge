'''
Created on 26.02.2013

@author: v.vlasov
'''

import Image
import os

print os.getcwd()

im = Image.open("..\\data\\oxygen.png")
pix = im.load()
s = ''
for hor in range(3, im.size[0], 7):
    s += chr(pix[hor, im.size[1]/2][0])

print s

list = [105, 110, 116, 101, 103, 114, 105, 116, 121]

o = ''
for i in list:
    o += chr(i)
    
print o