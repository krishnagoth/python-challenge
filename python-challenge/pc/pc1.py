'''
Created on 25.02.2013

@author: v.vlasov
'''
import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
newurl = "!#$%&()*+-<>@[]^_aeilqtuy{}"
revnewurl = "}{yutqliea_^][@><-+*)(&%$#!"
cry = 'ynnjw "kyn" in .../kyn.frkj'

print ''.join(map(lambda letter : letter if ord(letter) not in range(97, 123) else (chr(ord(letter) + 2) if ord(letter) in range(97, 121)  else chr(ord(letter) - 24)) , cry))

    
