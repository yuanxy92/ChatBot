import os
import socket
import time

from rasa_core.agent import Agent
agent = Agent.load("examples/restaurantbot/models/dialogue",
    interpreter="examples/restaurantbot/models/nlu/current")
agent.handle_message("hello")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',54377))
sock.listen(5)
print("start server")
while True:
    try:
        connection, address = sock.accept()
        print("client ip is:", address)
        buf = connection.recv(40960)
        out = agent.handle_message(buf)
        connection.sendall(out)
        print(out)
        connection.close()
        time.sleep(1)
    except KeyBoardInterrupt:
        connection.close()
        break

sock.close()