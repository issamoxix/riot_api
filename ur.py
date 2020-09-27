import requests as req
class requestss:
    def __init__(self,key,name,reg):
        self.key = key
        self.name = name
        self.req = reg
    #get account infos lvl , sumid , etc..
    def get_account_data(self):
        if self.req =='EUW' or self.req == "euw":
            reg = 'euw1'
            self.reg = reg
        elif self.req=='NA' or self.req =="na":
            reg = 'na1'
            self.reg = reg
        else: 
            return False
        typee="/summoner/v4/summoners/by-name/"
        url = "https://"+reg+".api.riotgames.com/lol"+typee+self.name+"?api_key="+self.key
        x = req.get(url)
        return x.json()
    #get infos about ranke
    def get_rank(self,s_id):
        typee="/league/v4/entries/by-summoner/"
        url = "https://"+self.reg+".api.riotgames.com/lol"+typee+s_id+"?api_key="+self.key
        x = req.get(url)
        return x.json()