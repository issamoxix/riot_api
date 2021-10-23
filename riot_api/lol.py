from riot_api import credentials
from links import Summby
from utils import getReq

class lol(credentials):
    game = "lol"

    def __init__(self,key,region="euw1"):
        credentials.__init__(self,key,region,game=self.game)
    
    def get_Summoner(self,value,by="name"):
        url = self.getUrl(api_type=Summby(value,by))
        return getReq(url)
        

