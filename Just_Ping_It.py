#This simple program pings any site or host you want
#and prints whether the host is up or down

import os
host = input("Enter IP address or Host name :")
ping = os.system("ping "+str(host))

if ping == 0:
    print("The host is UP!!!")
else:
    print("The host is DOWN :( ")
