'''
Created on 06.03.2013

@author: v.vlasov
'''

import Image
import ImageDraw

h = 480
w = 640

img_f = Image.open("..\\data\\p16\\mozart.gif", 'r')
in_pix = img_f.load()

print img_f

out_im = Image.new("P", (w * 2, h), (255))

prev_p = 0
shift = 0


for j in range(h):
    
    parr = []
    for i in range(w):
    
        p = in_pix[(i, j)]
        if p == 195:
            shift = 640 - i
        parr.append(p)
    for hor in range(w):
        out_im.putpixel((hor + shift, j), parr[hor])
       
out_im.show()
