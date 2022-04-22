def match_v5(var, by):
    # https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/7ss7pT0C2BublXr9SQtiQPqshug93qlkDwk3TP_6GQV6CvMG_AzGQWjwle1gwRop8QmrApP6t1Mihw/ids?start=0&count=20
    if by == "puuid":
        return f"match/v5/matches/by-puuid/{var}/ids"
    if by == "match_id":
        return f"match/v5/matches/{var}"
