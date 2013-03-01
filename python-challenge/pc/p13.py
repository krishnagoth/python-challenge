'''
Created on 28.02.2013

@author: Vladimir
'''

import httplib

body = '''<?xml version="1.0"?>
<methodCall>
  <methodName>phone</methodName>
  <params>
    <param>
        <value><string>555-ITALY</string></value>
    </param>
  </params>
</methodCall>'''


cli = httplib.HTTPConnection("www.pythonchallenge.com")



cli.request("POST", '/pc/phonebook.php', body)

resp = cli.getresponse()

print resp.read()