from main0 import *
import time , os




'''
#########COLOR VALUE #########


gy2="\033[30;2m"
rd2="\033[31;2m"
ge2="\033[32;2m"
ye2="\033[33;2m"
bl2="\033[34;2m"
pu2="\033[35;2m"
cy2="\033[36;2m"

gy1="\033[30;1m"
rd1="\033[31;1m"
ge1="\033[32;1m"
ye1="\033[33;1m"
bl1="\033[34;1m"
pu1="\033[35;1m"
cy2="\033[36;1m"

w0='\033[30;0m'

'''


a=Updown(146,2,2,)

inv1={'end_start':'\033[30;0m',"mod":"\033[30;0m","mid_mod":"\033[30;0m",'middle':'\033[30;2m','after_middle':'\033[30;2m',"default":"\033[30;0m"}
inv2={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m",'middle':'\033[30;0m','after_middle':'\033[30;0m',"default":"\033[30;0m"}



rw0={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m","middle":'\033[31;1m','after_middle':'\033[30;0m',"default":"\033[30;0m"}
rw1={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;2m","middle":'\033[31;1m','after_middle':'\033[30;1m',"default":"\033[30;0m"}
rw2={'end_start':'\033[30;2m',"mod":"\033[30;2m","mid_mod":"\033[30;0m","middle":'\033[31;2m','after_middle':'\033[30;1m',"default":"\033[30;0m"}




gb0={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m","middle":'\033[32;1m','after_middle':'\033[34;1m',"default":"\033[30;0m"}
gb1={'end_start':'\033[30;2m',"mod":"\033[30;2m","mid_mod":"\033[30;1m","middle":'\033[32;1m','after_middle':'\033[34;1m',"default":"\033[30;0m"}
gb2={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m","middle":'\033[32;2m','after_middle':'\033[34;2m',"default":"\033[30;0m"}



yc0={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m","middle":'\033[33;1m','after_middle':'\033[36;1m',"default":"\033[30;0m"}
yc1={'end_start':'\033[30;2m',"mod":"\033[30;2m","mid_mod":"\033[30;1m","middle":'\033[33;1m','after_middle':'\033[36;1m',"default":"\033[30;0m"}
yc2={'end_start':'\033[30;2m',"mod":"\033[30;0m","mid_mod":"\033[30;0m","middle":'\033[33;2m','after_middle':'\033[36;2m',"default":"\033[30;0m"}

def colfun(**color):
     
    print '\033[30;0m'+' '#,time.ctime()
    
    a.up(**color)
    a.middle(**color)
    a.middle2(**color)
    a.middle(**color)
    a.middle2(**color)
    a.middle(**color)
    a.down(**color)
    a.wait(2)
    print '\033[30;0m'+' '#,time.ctime()




colfun(**inv1)
colfun(**inv2)

colfun(**rw0)
colfun(**rw1)
colfun(**rw2)

colfun(**gb0)
colfun(**gb1)
colfun(**gb2)

colfun(**yc0)
colfun(**yc1)
colfun(**yc2)


