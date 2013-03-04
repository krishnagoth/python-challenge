'''
Created on 25.02.2013

@author: v.vlasov
'''
import httplib
import re

retdata = 'and the next nothing is 51350'
url = "/pc/def/linkedlist.php?nothing="

httpconn = httplib.HTTPConnection("www.pythonchallenge.com")

while retdata.rfind('and the next nothing is') != -1:
    httpconn.request("GET", url + re.findall("[0-9]+", retdata)[0])
    resp = httpconn.getresponse()
    retdata = resp.read()
    print retdata

