#This simple program pings any site or host you want
#use for pings
#provide the status whether the host is down or up!

import os
host = input("Provide the Required IP address else Name of host :")
ping = os.system("ping "+str(host))

if ping == 0:
    print("Congo! coz The host is up!!")
else:
    print("Sorry! yr host is DOWN :( ")
