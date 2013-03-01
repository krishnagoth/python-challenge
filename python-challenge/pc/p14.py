'''
Created on 28.02.2013

@author: Vladimir
'''

from PIL import Image
from PIL import ImageDraw

size = 100

img_f = Image.open("data\\p14\\wire.png", 'r')
in_pix = img_f.load()
out_im = Image.new("RGB", (size, size), (255, 255, 255, 255))

data_arr = []

r = -1

pos = []

class PrevPos():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        
    def shift(self, x, dir):
        if x:
            self.pos_x += dir
        else:
            self.pos_y += dir
        
        print (self.pos_x, self.pos_y)
        return (self.pos_x, self.pos_y)
    


pos.append((0,0))

for i in range(0, 100):
    pos.append((i,0))
    
prev_pos = PrevPos(99,0)

for i in range(99, 1, -1):
    for j in range(0,i):
        pos.append(prev_pos.shift(False, -(1 - (i%2)*2)))
    for j in range(0,i):
        pos.append(prev_pos.shift(True, (1 - (i%2)*2)))
        
print len(pos)    
def get_next_pos():
    global r
    global pos
    r+=1
    if (r < len(pos)):
        return pos[r]
    else:
        return pos[len(pos) - 1]

for hor in range(10000):
    out_im.putpixel(get_next_pos(), in_pix[hor, 0])

out_im.show()
