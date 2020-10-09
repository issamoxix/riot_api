import requests as req
class requestss:
    def __init__(self,key,name,reg):
        self.key = key
        self.name = name
        self.reg = False
        self.req = reg
        self.error = False
        self.reg_tp= {'euw':'euw1','na':'na1'}
        typee = None
        self.url = "https://"+str(self.req)+".api.riotgames.com/lol"+str(typee)+"?api_key="+str(self.key)
    #get account infos lvl , sumid , etc..
    def get_account_data(self):
        for i in self.reg_tp:
            if self.req.lower() == i:
                self.reg = self.reg_tp[i]
        if not self.reg:
            self.error = 'Error : The region you have chosen is wrong'
            return self.error
        typee="/summoner/v4/summoners/by-name/"
        url = "https://"+str(self.reg)+".api.riotgames.com/lol"+str(typee)+str(self.name)+"?api_key="+str(self.key)
        x = req.get(url)
        return x.json()
    #get infos about ranke
    def get_rank(self,s_id):
        typee="/league/v4/entries/by-summoner/"
        url = "https://"+self.reg+".api.riotgames.com/lol"+typee+s_id+"?api_key="+self.key
        x = req.get(url)
        return x.json()
    def get_match_history(self,s_id):
        typee ="/match/v4/matchlists/by-account/"
        url ="https://"+self.reg+".api.riotgames.com/lol"+typee+s_id+"?api_key="+self.key
        x = req.get(url)
        return x.json()
