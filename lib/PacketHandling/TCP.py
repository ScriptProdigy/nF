import socket
import threading

class TCPClient:
    def __init__(self, IP, PORT, BUFFERSIZE=1024):
        self.s = socket.socket()
        self.Server_IP = IP
        self.Server_PORT = PORT
        self.BUFFERSIZE = BUFFERSIZE

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((IP, PORT))

        self.ReceivedPackets = []

        self.Recv = True
        T = threading.Thread(target=self.RecvThread)
        T.start()

    def RecvThread(self):
        while self.Recv:
            data = self.s.recv(self.BUFFERSIZE)
            if(len(data) > 0):
                self.ReceivedPackets.append(data)
                    
    def GetReceivedPackets(self):
        Ret = self.ReceivedPackets
        self.ReceivedPackets = []
        return Ret

    def SendPacket(self, Packet):
        self.s.send(Packet + chr(0))