'''
Created on 12.03.2013

@author: Vladimir
'''

import difflib

f = open('..\\data\\p18\\delta.txt', 'rb')

left, right = [], []

for row in f:
    row = row.replace('\n', '')
    left.append(row[:53])
    right.append(row[56:])

print left
print right

f.close()
    
diff = list(difflib.ndiff(left,right))

png = ['', '' , '']

for row in diff:
    bytes = [chr(int(byte,16)) for byte in row[2:].split()]
    if row[0]=='-': png[0]+=''.join(bytes)
    elif row[0]=='+': png[1]+=''.join(bytes)
    elif row[0]==' ': png[2]+=''.join(bytes)

for i in range(3):
    open('..\\data\\p18\\out%d' %i,'wb').write(png[i])