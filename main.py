from lib import GZL
from getpass import getpass

class Main:
    def __init__(self):
        self.GZL = GZL.GaiaZomgLib()

    def Run(self):
        while(self.GZL.login("TheManx2", getpass("Password: ")) == False):
            pass ## While we can't login, fuck everything else and retry.

        #print self.GZL.GSI.get_zomg_servers(self.GZL.GSid)
        ####
        ## This is what I want to be able to do. This friggin' easy.
        ####
        self.GZL.startup()
        # while(True):
        #     Pos = self.GZL.get_position()
        #     Sel_Mob = self.GZL.get_nearest_monster(Pos)
        #     self.GZL.attack(Sel_Mob)

        ####
        ## NO PACKET HANDLING IN MAIN CLASS MATT, BAD IDEA FUCKER
        ####
        # self.GZL.PH.Send("<msg t='sys'><body action='verChk' r='0'><ver v='141' /></body></msg>" + chr(0))

        # while(True):
        #     Packets = self.GZL.PH.TCP.GetReceivedPackets()
        #     if(len(Packets) != 0):
        #         print Packets


if(__name__=="__main__"):
    M = Main()
    M.Run()