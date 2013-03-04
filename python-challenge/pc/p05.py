'''
Created on 25.02.2013

@author: v.vlasov
'''
import pickle
from pickle import Unpickler
import cPickle

data_file = open("testdata\\p5.data")
pick = cPickle.load(data_file)

src = [1, 1, [2], 1, [2, 2, 2], [2, 2], [2, [3, 3], [3, 3], 2, 2, [3, [4, 4]]], 1, 1]

def print_every_line(source, level):
    for line in source:
        if type(line) == list:
            print_every_line(line, level + 1)
        else:
            print '-'*level + str(line)

def print_new_line(source, level):
        
    print '-'*level,
    for line in source:
        if type(line) == list:
            print
            print_new_line(line, level + 1)
        else:
            print line,
        
    print '\n' + '-'*(level - 1),

print_new_line(pick, 1)
print '='*20

outfile = open("out.b", 'w')

for line in pick:
    s = ''
    for tup in line:
        s += tup[0]*tup[1]
    print s
        
outfile.close()

