
mid_iter=2
mid=1
def up():
   i=0
   while i<20 :
       length_ends=(length_max-mid)/2
       print '*'*length_ends,'0'*mid,'*'*length_ends
       i+=1
       if (i%mid_iter)==0 :
           mid+=2
   
def down():
   i=0
   while i<=4 :
      length_ends=(length_max-mid)/2
      print '*'*length_ends,'0'*mid,'*'*length_ends
      i+=1
      mid-=4
