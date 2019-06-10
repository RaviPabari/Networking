#using this simple python program you can find IP address of any site
#just like pinging a host it returns a IP

import socket
import os
from getch import pause
a = input("Enter host name for eg 'www.google.com' " + "\n"+ "--->")
ip = socket.gethostbyname(a)
print(ip)
pause()
