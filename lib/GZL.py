from PacketHandling import PH
from GSI import GSI
import HttpWrapper

class GaiaZomgLib:

    class GaiaConstants:
        HOMEPAGE = "http://www.gaiaonline.com/"

        GSI = HOMEPAGE + "chat/gsi/index.php"
        LOGIN_PAGE = HOMEPAGE + "auth/login/"

    class Monster:
        ID = ""
        Name = ""
        Position = { "map_name": "", "x": 0, "y": 0 }
        Level = 0

    def __init__(self):
        self.username = ""
        self.password = ""
        self.LoggedIn = False
        self.GSid = ""

        self.HTTP = HttpWrapper.HTTPWrapper()
        self.GSI = GSI.GSI(self)
        self.PH = PH.PacketHandler(self)

    def login(self, Username, Password):
        self.username = Username
        self.password = Password

        if(self.LoggedIn == True):
            return True

        params = dict()
        Req = self.HTTP.Req(self.GaiaConstants.LOGIN_PAGE)

        Req = Req.replace("\t", " ").replace("\n", "").replace("    ", " ").replace('data-value', 'data')
        #print "req"
        data = self.HTTP.GetBetween(Req, '<form action="/auth/login/" id="memberloginForm" method="post">', '</form>')
        #print data

        for x in xrange(0, data.count('input')-1):                     ### Due to randomization of the order, and a hidden value that has a random name/value,
                                                                       ### I am just building post data automatically. Then modify user/pass later.
            try:
                complete =  self.HTTP.GetBetween(data, '<input', '/>')
                name =  self.HTTP.GetBetween(complete, 'name="', '"')
                value =  self.HTTP.GetBetween(complete, 'value="', '"')
                params[name] = value
                data = data.split(complete)[1]
            except:
                pass

        params['username'] = Username
        params['password'] = Password
        params['chap'] = ''
        params['redirect'] = self.GaiaConstants.HOMEPAGE
        params['signInButton'] = 'Log+In'

        Login_Req = self.HTTP.Req(self.GaiaConstants.LOGIN_PAGE, params)
        if('View or change your Account Settings' in Login_Req):
            self.LoggedIn = True
            self.GSid = self.GSI.get_gsid()
            return True
        else:
            self.LoggedIn = False
            return False

    def startup(self):
        if(self.LoggedIn == False):
            return False

        ####
        ## Need to send the following packets, which require the packet id after
        ####

        #######
        ##
        ## Login Packet; 
        ## {'args': {'cmd': u'playerInfo', 'parameters': None}, 'type': 1, 'name': u'battleCommand', 'cid': self.GetNewCID()}, Encode=True
        ##
        ###
        ### After Reply From playerInfo:
        ###
        ### {'args': {'cmd': u'getNkvp', 'parameters': {'keys': [u'musicVolume', u'soundVolume', u'musicState']}}, 'type': 1, 'name': u'battleCommand', 'cid': self.GetNewCID()}, Encode=True)
        ### {'args': {'cmd': u'clientFlashStats', 'parameters': {'os': u'Windows 7', 'flashVersion': u'WIN 11,1,102,62', 'screenResolutionY': 900, 'screenResolutionX': 1600}}, 'type': 1, 'name': u'battleCommand', 'cid': self.GetNewCID()}, Encode=True)
        ####
        #### After Reply From getInventoryInfo
        #### 
        #### {'args': {'cmd': u'version', 'parameters': {}}, 'type': 1, 'name': u'battleCommand', 'cid': self.GetNewCID()}, Encode=True)
        #####
        ##### After Reply From version
        #####
        ##### {'args': {'cmd': u'getGlobals', 'parameters': {}}, 'type': 1, 'name': u'battleCommand', 'cid': self.GetNewCID()}, Encode=True)
        #######


    def send_chat(self, message):
        return False

    def send_move(self, toPos):
        return False

    def get_position(self):
        return {"map_name": "", "x": 0, "y": 0}

    def get_chat(self):
        return [
            {
                "id": "0",
                "from": "4556",
                "message": "fdas",
                "chat_group": "Global"
            },
            {
                "id": "1",
                "from": "1541564",
                "message": "fdas",
                "chat_group": "Global"
            }
        ]