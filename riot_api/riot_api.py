from riot_api import credentials,getRank

class RiotApi(credentials,getRank):
    version= 1.0
    def __init__(self,key,username):
        credentials.__init__(self,key,username)
        getRank.__init__(self)
        pass