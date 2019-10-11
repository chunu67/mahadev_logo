#########COLOR VALUE #########
'''

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
'''
w0='\033[30;0m'

##Used for testing ###

for i in range(30,37):
 code1='\033['+str(i)+';1m'
 #print code ,code+'hello'
for i in range(30,37):
 code2='\033['+str(i)+';2m'
 print code1+'hello1',code2+'hello2' #+w0

###################################################
