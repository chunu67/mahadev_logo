


length_max = 146
length_end = 10
mid_afters = 0
mid = 0

loop_line=0

# Str Values 

e=''
m_f=''
m=''

mid_iter = 0


p = 0 # it is value for mid
pe = 0  # it is increaser for p


def fun(p,pe,mid_iter):
    length_end=10
    loop_lines=1
    mid=0
    while loop_lines <= 10 :

        mid+=(p+pe)

        mid_afters = int(length_max-(length_end*2))-mid

        print '0'*length_end,'@'*(mid_afters/2),'#'*mid,'@'*(mid_afters/2),'0'*length_end
        print loop_lines,length_end,mid_afters,mid,mid_afters,length_end

        if loop_lines < 5 :
           length_end -= 2
        elif loop_lines==5 : 
           length_end=2
        #elif loop_lines==6 :
        #    length_end=2
        else : #loop_lines >= 5 
           length_end +=2

        #else :
         #  length_end += 2
        #########################-----MID--###################
        #if (loop_lines%mid_iter)==0 :
        #   pe+=2

        loop_lines += 1

       #print pe
#print '0'.center(151,'#')

fun(1,6,4)
fun(2,4,6)









