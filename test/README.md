
COLOR0='\033[30;0m'
COLOR1='\033[30;1m'
COLOR2='\033[30;2m'


## Make sense of color printing  in Linux Shell ##  

1. '\033[n;0m' will be print as a simple white color like '\033[30;0m'  if you put it  in front of first word in a line  .
2. or if you put it in a variable and then concatinate with a string ...... it react same

	like ''' value='\033[n;0m' ; print value + 'It is My String'   '''



3. So that alaways put '\033[n;1m' in front of a line 


4. if you  put it before  '\033[n;2m'  it will be printed  as COLOR2  


5.## Solution of printing ## 

  for printing COLOR0  put  in front of line 'COLOR0'+'COLOR1'
  for printing COLOR1  put  in front of line 'COLOR1'+'COLOR1'
  for printing COLOR2  put  in front of line 'COLOR0'+'COLOR2'
