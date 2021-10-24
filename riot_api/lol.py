from riot_api import credentials
from links import Summby,ChampMystery,getRankInfo
from utils import getReq

class lol(credentials):
    game = "lol"

    def __init__(self,key,region="euw1"):
        credentials.__init__(self,key,region,game=self.game)
    
    def get_Summoner(self,value,by="name"):
        url = self.getUrl(api_type=Summby(value,by))
        return getReq(url)

    def get_ChampionMastery(self,value,by=None,championId=None,get_total_score=False):
        url = self.getUrl(api_type=ChampMystery(value,by,championId,get_total_score))
        return getReq(url)

    def get_Rank(self,value,by="id"):
        url = self.getUrl(api_type=getRankInfo(var=value,by=by))
        return getReq(url)
        

