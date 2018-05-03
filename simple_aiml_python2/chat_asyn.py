import aiml
import asyncore
import os
os.chdir('./alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
print alice.respond('LOAD ALICE')
print alice.respond('hello')

import socket
import time

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        try:
            data = self.recv(40960)
        except KeyboardInterrupt:
            print "Crtl+C pressed. Shutting down." 
        if data:
            out = alice.respond(data)
            self.sendall(out)
            print out
            self.close()

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print "client ip is:", addr
            handler = EchoHandler(sock)

server = EchoServer('127.0.0.1', 54377)
asyncore.loop()