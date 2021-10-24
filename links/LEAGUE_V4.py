def getRankInfo(var,by="id"):
    if by == 'id':
        return f"league/v4/entries/by-summoner/{var}"