'''
Created on 13.03.2013

@author: Vladimir
'''

import array, wave
wi = wave.open('..\\data\\p19\\indian.wav', 'rb')
wo = wave.open('..\\data\\p19\\indian_inv.wav', 'wb')
wo.setparams(wi.getparams())
a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()
wo.writeframes(a.tostring())
wi.close(), wo.close()
