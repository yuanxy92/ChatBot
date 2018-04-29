import aiml
import os
os.chdir('./alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
print alice.respond('LOAD ALICE')
print alice.respond('hello')

import socket
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',54377))
sock.listen(5)
print "start server"
while True:
    connection, address = sock.accept()
    print "client ip is:", address
    buf = connection.recv(40960)
    out = alice.respond(buf)
    connection.sendall(out)
    print out
    connection.close()
    time.sleep(1)

sock.close()