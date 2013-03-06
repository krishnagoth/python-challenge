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
out_im = Image.new("RGB", (w * 2, h), (255, 255, 255, 255))

prev_p = 0

for j in range(h):
    for i in range(w):
    
        p = in_pix[(i, 0)]
        if p == 195:
            pp = in_pix.index(p)
            for hor in range(w):
                out_im.putpixel((hor + 640 - pp[0], pp[1]), p)
       
out_im.show()
