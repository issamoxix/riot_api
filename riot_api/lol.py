from riot_api import credentials
from links import Summby, ChampMystery, getRankInfo, match_v5
from utils import getReq


class lol(credentials):
    game = "lol"

    def __init__(self, key, region="euw1"):
        self.region = region
        self.key = key
        credentials.__init__(self, self.key, self.region, game=self.game)

    def get_Summoner(self, value, by="name", region="euw1"):
        self.region = region
        url = self.getUrl(api_type=Summby(value, by))
        return getReq(url, self.key)

    def get_ChampionMastery(
        self, value, by=None, championId=None, get_total_score=False
    ):
        url = self.getUrl(api_type=ChampMystery(value, by, championId, get_total_score))
        return getReq(url, self.key)

    # riot doc https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
    def get_Rank(self, value, by="id"):
        url = self.getUrl(api_type=getRankInfo(var=value, by=by))
        return getReq(url, self.key)

    # get_match has optional params check here https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID
    def get_match(self, value, by="ids", **params):
        self.region = "europe"
        url = self.getUrl(api_type=match_v5(var=value, by=by))
        if by == "match_id":
            match = getReq(url, key=self.key, optional_kwargs=params)
            participants = match.get("info").get("participants")
            for participant in participants:
                participant_puuid = participant.get("puuid", "0")
                participant_details = self.get_Summoner(
                    value=participant_puuid, by="puuid"
                )
                participant["player_name"] = participant_details.get("name")
                participant["player_details"] = participant_details
            return match
        return getReq(url, key=self.key, optional_kwargs=params)
