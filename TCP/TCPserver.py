#A very basic TCP program to connect a client and server to stream(or send) data
import socket
                                                         #we dont need to define host or ip in server side because the OS does it :)
sport = 12000                                            #We have to operate server on particular server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #AF=address family,INET = ipv4,INET6 = ipv6, STREAM = TCP, DGRAM = UDP
s.bind((socket.gethostname(),sport))                     #note bind only take one arguement thats why we have used ( (x,y) )
s.listen(2)                                              #note here our queue is of 2 means our server can only handle 2 concetions
print("The server is ready to recieve: ")

while True:
    clientsocket, address = s.accept()
    print("Connection from" + str(address) + " has been established!")

    clientsocket.send(bytes("welcome to the jungle!","utf-8"))
