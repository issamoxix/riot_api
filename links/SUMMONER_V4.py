def Summby(var,by):
    if by == 'name':
        return f"summoner/v4/summoners/by-name/{var}"
    if by == "account_id":
        return f"summoner/v4/summoners/by-account/{var}"
    if by == "puuid":
        return f"summoner/v4/summoners/by-puuid/{var}"
    if by == "id":
        return f"summoner/v4/summoners/{var}"
