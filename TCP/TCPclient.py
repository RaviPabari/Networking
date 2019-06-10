import socket
sport = 12000                               #use any port which are not in use by OS or are generally not used by OS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),sport))     #directly giving host name by function socket.gethostname
while True:
    msg = s.recv(1024)                      #note we have to maintain buffer size equal both side
    print(msg.decode("UTF-8"))              #we have used while loop here bec if in case of low buffer size
                                            #we will only recieve the data size of buffer so by keeping in loop we can recv all data :)
                                            
