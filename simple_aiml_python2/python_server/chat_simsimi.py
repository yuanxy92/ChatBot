import os
import socket
import time
import sys
import urllib
import urllib2

if __name__ == '__main__':
    print 'PID of current python script is ', os.getpid()


    url = "http://sandbox.api.simsimi.com/request.p?key=7e9ce751-34ca-47c8-8b2e-6015a1a56ef1&lc=en&ft=1.0&"
    
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

            values = {} 
            values['text'] = buf
            request = urllib2.Request(url + urllib.urlencode(values))
            print (url + urllib.urlencode(values))
            response_post = urllib2.urlopen(request)
            out = response_post.read().decode("utf-8")

            connection.sendall(out)
            print out
            connection.close()
        time.sleep(1)
    
    # exit
    sock.close()