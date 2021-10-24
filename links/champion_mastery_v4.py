def ChampMystery(var,by,championId=None,get_total_score=False):
    if by == "id":
        return f"champion-mastery/v4/champion-masteries/by-summoner/{var}"
    if by =="champ_id":
        return f"champion-mastery/v4/champion-masteries/by-summoner/{var}/by-champion/{championId}"
    if get_total_score:
        return f"champion-mastery/v4/scores/by-summoner/{var}"

