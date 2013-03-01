'''
Created on 27.02.2013

@author: Vladimir
'''

num = 5
origfile = open("data\\evil2.gfx", 'rb')
filearr = []

strarr = []

for n in range(num):
    filearr.append(open("data\\p11\\out" + str(n), 'wb'))
    strarr.append('')

file_ctr = -1

def next_ind():
    global file_ctr
    
    file_ctr += 1
    
    if (file_ctr == num):
        file_ctr = 0    
    return file_ctr

bline = origfile.read()


for b in bline:
    strarr[next_ind()] += b

for n in range(num):
    filearr[n].write(strarr[n])
    filearr[n].close()