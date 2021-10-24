from riot_api import lol

if __name__ == '__main__':
    RiotApi = lol(key="RGAPI-a2e33ed9-951b-49f8-aaa3-4b50687bedc9")
    response = RiotApi.get_Summoner(value="taoufique",by="name")
    ChampMystery = RiotApi.get_ChampionMastery(value=response['id'],get_total_score=True)
    getRank = RiotApi.get_Rank(value=response['id'])
    print(getRank)