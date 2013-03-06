'''
Created on 04.03.2013

@author: Vladimir
'''

import random
import sys
import threading

def getseed(word):
    
    print 'Searhing seed for', word
    
    k = -sys.maxint - 1
    
    offset = 96
    
    while k < sys.maxint:
        a = [ord(let) for let in word]
        b = []
        random.seed(k)
        for i in range(len(a)):
            sym = random.randint(0, 26)
            if a[i] == offset + sym:
                b.append(sym)
            else:
                break
        else:
            print k, word, b
            break
        k += 1

class thrd(threading.Thread):
    def __init__(self, word):
        self.word = word
        threading.Thread.__init__(self)
    def run(self):
        getseed(self.word)
        
th1 = thrd("hello")
th2 = thrd("world")

#th1.start()
#th2.start()

#th1.join()
#th2.join()
 
# -2145353394 hello 
# -2141522982 world

getseed("hello")
getseed("world")