from time import sleep
import os



#1 end-start  es
#2 mid        md
#3 mid_after  mf
W='\033[30;0m'
class Updown :

    def __init__(self,length_max,mid_iter,mid,**color):
        self.length_max=length_max
        self.mid_iter=mid_iter
        self.mid=mid
        #self.data=data
        #self.length_ends=0
        #self.es=color['end_start']
        #self.md=color['middle']
        #self.mf=color['after_middle']            # Color $after_middle is used for modifing and define `md( middle colour )` 
        #self.df=color['default']
        #self.mod=color['mod']                     # Color $mod is used for modifing and define `md( middle colour )` 
        #self.mid_mod=color['mid_mod']
 




#############################__________UP______########################################################   





    def up(self,**color):
        es=color['end_start']
        md=color['middle']
        mf=color['after_middle']
        df=color['default']
        mod=color['mod'] 
        mid_mod=color['mid_mod'] 
        i=0
        #print self.data
        while i<20 :
            
            self.length_ends=(self.length_max-self.mid)/2
            #print self.mid
            print df+es+('*'*self.length_ends),mid_mod+md+('#'*self.mid),df+es+('*'*self.length_ends)
            i+=1
            if (i%self.mid_iter)==0 :
                self.mid+=2
        
        




###########################________middle_______#####################################################i

    def middle(self,**color):
        es=color['end_start']
        md=color['middle']
        mf=color['after_middle']
        df=color['default']
        mod=color['mod'] 
        mid_mod=color['mid_mod'] 
        length_end=10         
        loop_lines=1
        while loop_lines <= 10 :



            mid_afters = int((self.length_max-2)-(length_end*2))-self.mid

            print df+es+('0'*length_end),mod+mf+('@'*(mid_afters/2)),mid_mod+md+('#'*self.mid),mod+mf+('@'*(mid_afters/2)),df+es+('0'*length_end)
            #print loop_lines,length_end,mid_afters,self.mid,mid_afters,length_end

            if loop_lines < 5 :
               length_end -= 2
            elif loop_lines==5 :
               length_end=2
            #elif loop_lindf+es==6 :
            #    length_end=2
            else : #loop_lindf+es >= 5
               length_end +=2
            #else :
             #  length_end += 2
        #########################-----MID----###################
        #if (loop_lines%mid_iter)==0 :
          # pe+=2

            loop_lines += 1 
        
        
##############################_______Middle2______##################################################

    def middle2(self,**color):
        es=color['end_start']
        md=color['middle']
        mf=color['after_middle']
        df=color['default']
        mod=color['mod'] 
        mid_mod=color['mid_mod'] 
        i=0
        #print self.data
        while i<10 :

            self.length_ends=(self.length_max-self.mid)/2
            #print self.mid
            print df+es+('*'*self.length_ends),mid_mod+md+('#'*self.mid),df+es+('*'*self.length_ends)
            i+=1



###############################________Down________##################################################

    
    def down(self,**color):
        es=color['end_start']
        md=color['middle']
        mf=color['after_middle']
        df=color['default']
        mod=color['mod'] 
        mid_mod=color['mid_mod'] 

        i=0
        while i<=4 :
            self.length_ends=(self.length_max-self.mid)/2
            print df+es+('*'*self.length_ends),mid_mod+md+('#'*self.mid),df+es+('*'*self.length_ends)
            i+=1
            self.mid-=4
    def wait(self,t):
        sleep(t)
        os.system('clear')
