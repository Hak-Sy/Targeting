#!/usr/bin/python

#----------------------------------------
#| Code => Hak-Sy       		|
#| Fb => hosam.ahmad2017                |
#| Gmail => hosamalshami019@gmail.com   |
#| From = > Syria                       |
#----------------------------------------

from googlesearch import *
from sys import *
def sql():

    baner=print ('''

\033[1;91m                                    l:::::l
                                    l:::::l 
                                    l:::::l 
                                    l:::::l 
    ssssssssss      qqqqqqqqqqqqqqqqql::::l 
  ss::::::::::s    q:::::::::qqq::::ql::::l 
ss:::::::::::::s  q:::::::::::::::::ql::::l 
s::::::ssss:::::sq::::::qqqqq::::::qql::::l 
 s:::::s  ssssss q:::::q     q:::::q l::::l 
   s::::::s      q:::::q     q:::::q l::::l 
      s::::::s   q:::::q     q:::::q l::::l 
ssssss   s:::::s q::::::q    q:::::q l::::l 
s:::::ssss::::::sq:::::::qqqqq:::::ql::::::l
s::::::::::::::s  q::::::::::::::::ql::::::l
 s:::::::::::ss    qq::::::::::::::ql::::::l
  sssssssssss        qqqqqqqq::::::qllllllll
                             q:::::q        
                             q:::::q        
                            q:::::::q       
                            q:::::::q       
                            q:::::::q       
                            qqqqqqqqq

''')

    
    dork=input ('\033[94mEnter the dork here : ')
    for dorks in search (dork):
            print (dorks)
            with open('website-sql.txt',mode='a') as f :
                f.write (dorks+'\n')
