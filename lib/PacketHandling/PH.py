import pyamf
import base64
import binascii

import TCP

class PacketHandler:

    class PacketDefs:
        class Recv:


        class Send:

    def __init__(self, GaiaZomgLib, IP='208.85.93.217', PORT=8080):
        self.GaiaZomgLib = GaiaZomgLib
        self.TCP = TCP.TCPClient(IP, PORT, 1024) 

    def Send(self, Data, Encode=False):  ## Send as Dict or Str ! :D Auto makes it json string if Encode is true and Data is dict
        Pkt = Data
        if(Encode):
            Pkt_Encoded = self.B64_to_AMF3(Pkt)
            Pkt = "%xt%G_BT_PLUGIN%battleCommand%-1%" + str(Pkt_Encoded) + "%"

        #print "SENDING " + Pkt
        self.TCP.SendPacket(Pkt)
        return Pkt

    def B64_to_AMF3(self, Packet):
        AMF3 = pyamf.encode(Packet,encoding=3).read()
        return base64.b64encode(str(AMF3))

    def AMF3_to_B64(self, Packet):
        Data = base64.b64decode(Packet)
        Ret = []
        for obj in pyamf.decode(Data):
            Ret.append(obj)
        return Ret

    def Decode_HEX(self, Hex):
        return binascii.unhexlify(Hex)


