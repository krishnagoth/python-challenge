'''
Created on 26.02.2013

@author: v.vlasov
'''

import zipfile
import re

arch = zipfile.ZipFile("testdata\\channel.zip", 'r')
print arch.namelist()
print arch.extract("readme.txt")

next_name = '90052.txt'

history = []

while next_name != '.txt':
    history.append(next_name)
    file_name = arch.extract(next_name, "testdata\\p6")
    line = open(file_name).readline()
    print line
    next_name = ''.join(re.findall("[0-9]*", line)) + ".txt"

print ''.join([arch.getinfo(i).comment for i in history])