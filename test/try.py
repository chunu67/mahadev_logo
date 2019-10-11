from testud import *
import time





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

inv1={'es':'\033[30;0m','md':'\033[30;2m','mf':'\033[30;2m'}
inv2={'es':'\033[30;1m','md':'\033[30;0m','mf':'\033[30;0m'}


rw1={'es':'\033[30;1m','md':'\033[31;1m','mf':'\033[30;0m'}
rw2={'es':'\033[30;2m','md':'\033[31;2m','mf':'\033[30;0m'}


gb1={'es':'\033[30;1m','md':'\033[32;1m','mf':'\033[34;1m'}
gb2={'es':'\033[30;2m','md':'\033[32;2m','mf':'\033[34;2m'}


yc1={'es':'\033[30;1m','md':'\033[33;1m','mf':'\033[36;1m'}
yc2={'es':'\033[30;2m','md':'\033[33;2m','mf':'\033[36;2m'}

def colfun(**color):

    print '\033[30;0m'+' ',time.ctime()

    a.up(**color)
    a.middle(**color)
    a.middle2(**color)
    a.middle(**color)
    a.middle2(**color)
    a.middle(**color)
    a.down(**color)

    #print '\033[30;0m'+' ',time.ctime()





#colfun(**inv1)
colfun(**inv2)



colfun(**rw1)
colfun(**rw2)

colfun(**gb1)
colfun(**gb2)

colfun(**yc1)
colfun(**yc2)


