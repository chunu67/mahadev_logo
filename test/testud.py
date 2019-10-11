




#1 end-start  es
#2 mid        md
#3 mid_afetrs mf

class Updown :

    def __init__(self,length_max,mid_iter,mid):
         self.length_max=length_max
         self.mid_iter=mid_iter
         self.mid=mid
         #self.data=data
         #self.length_ends=0
   
    def up(self,**color):
        es=color['es']
        md=color['md']
        mf=color['mf']
        i=0
        #print self.data
        while i<20 :
            
            self.length_ends=(self.length_max-self.mid)/2
            #print self.mid
            print es+('*'*self.length_ends),md+('0'*self.mid),es+('*'*self.length_ends)
            i+=1
            if (i%self.mid_iter)==0 :
                self.mid+=2
        
        




################################################################################i

    def middle(self,**color):
        es=color['es']
        md=color['md']
        mf=color['mf']
        length_end=10
        loop_lines=1
        while loop_lines <= 10 :



            mid_afters = int((self.length_max-2)-(length_end*2))-self.mid

            print es+('0'*length_end),mf+('@'*(mid_afters/2)),md+('#'*self.mid),mf+('@'*(mid_afters/2)),es+('0'*length_end)
            #print loop_lines,length_end,mid_afters,self.mid,mid_afters,length_end

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
        #########################-----MID----###################
        #if (loop_lines%mid_iter)==0 :
          # pe+=2

            loop_lines += 1 
        
        
################################################################################

    def middle2(self,**color):
        es=color['es']
        md=color['md']
        mf=color['mf']
        i=0
        #print self.data
        while i<10 :

            self.length_ends=(self.length_max-self.mid)/2
            #print self.mid
            print es+('*'*self.length_ends),md+('#'*self.mid),es+('*'*self.length_ends)
            i+=1



#################################################################################

    
    def down(self,**color):
        es=color['es']
        md=color['md']
        mf=color['mf']
        i=0
        while i<=4 :
            self.length_ends=(self.length_max-self.mid)/2
            print es+('*'*self.length_ends),md+('0'*self.mid),es+('*'*self.length_ends)
            i+=1
            self.mid-=4
        
