'''
Created on 27.02.2013

@author: Vladimir
'''
from encodings import utf_8
from encodings.base64_codec import base64_decode
import base64
import zlib
import gzip
import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pa = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

und = bz2.decompress(un)
pad = bz2.decompress(pa)

print und 
print pad