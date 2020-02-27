#Socket client example in python
 
import socket   #for sockets
 
#create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print('Socket Created')