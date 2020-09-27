import ur
import requests as req
class summoner :
    def __init__(self,name,api_key,reg):
        self.name = name
        self.key = api_key
        self.reg = reg
        self.get_account()
    def get_account(self):
        req = ur.requestss(self.key,self.name,self.reg)
        data = req.get_account_data()
        self.id = data['id']
        self.accountId = data['accountId']
        self.puuid = data['puuid']
        self.profileIconId = data['profileIconId']
        self.summonerLevel = data['summonerLevel']
        self.revisionDate = data['revisionDate']
        rank_data = req.get_rank(self.id)
        self.rank_d = rank_data
        if len(rank_data) ==1:
            self.rank_data = rank_data[0]
            self.win_rate = str((self.rank_data['wins']*100)//(self.rank_data['wins']+self.rank_data['losses'])) +"%"
        elif len(rank_data) ==0:
            self.rank_data = "Unranked"
    def res(self):
        print('Name : ',self.name)
        print('Lvl : ',self.summonerLevel)
        if len(self.rank_d) ==1:
            print('Rank :',self.rank_data['tier'], self.rank_data['rank'])
            print('Win Rate :',self.win_rate)
        else:
            print('Rank : ',self.rank_data)
        
        
# key = "RGAPI-3bc32b8b-5bc9-44fb-990b-ff963729a790"
# summoner = summoner('taoufique',key,'euw')
