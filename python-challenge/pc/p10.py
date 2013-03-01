'''
Created on 27.02.2013

@author: Vladimir
'''

start = 1

def getnext(val):
    str_val = str(val)
    prev_i = str_val[0]
    str_val = str_val[1:]
    buff = [prev_i]
    output = ''
    for i in str_val:
        if i == prev_i:
            buff.append(int(i))            
        else:
            output += str(len(buff)) + str(prev_i)
            buff = [i]
        prev_i = i
    output += str(len(buff)) + str(prev_i)
    return output

a = [1]

for ctr in range(30):
    a.append(getnext(a[ctr]))

print a

print len(a[30])