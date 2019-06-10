import socket
import os
from getch import pause
a = input("Enter host name for eg 'www.google.com' " + "\n"+ "--->")
ip = socket.gethostbyname(a)
print(ip)
pause()
