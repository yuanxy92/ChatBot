import aiml
import os
import socket
import time
import sys

def load_aiml(dir):
    os.chdir(dir + '\\alice')
    alice = aiml.Kernel()
    alice.learn("startup.xml")
    print alice.respond('LOAD ALICE')
    print alice.respond('hello')
    return alice


if __name__ == '__main__':
    print 'PID of current python script is ', os.getpid()

    # load aloce aiml
    alice = load_aiml(sys.argv[1])

    # init socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',54377))
    sock.listen(5)
    print "start server"

    # main loop
    while True:
        connection, address = sock.accept()
        print "client ip is:", address
        buf = connection.recv(40960)
        if cmp(buf, 'getpid') == 0:
            pid = os.getpid()
            connection.sendall(str(pid))
            connection.close()
        else:
            out = alice.respond(buf)
            connection.sendall(out)
            print out
            connection.close()
        time.sleep(1)
    
    # exit
    sock.close()