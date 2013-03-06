'''
Created on 06.03.2013

@author: v.vlasov
'''

import calendar
import datetime

for i in range(1006, 1997, 10):
    dt = datetime.date(i, 1, 26)
    if dt.weekday() == 0 and calendar.isleap(i):
        print i 

# answ: mozart