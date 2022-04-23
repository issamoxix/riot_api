from riot_api import lol

KEY = "ROIT_API_KEY"


if __name__ == "__main__":

    riot_api = lol(key=KEY)
    player_details = riot_api.get_Summoner(value="taoufique", by="name")
    puuid = player_details.get("puuid", "")
    matches_id = riot_api.get_match(value=puuid, by="puuid", start=0, count=100)
    # print(get_matches_id)
    match = riot_api.get_match(value=matches_id[0], by="match_id")
    # participants = match.get("info").get("participants")
    # for participant in participants:
    #     participant_puuid = participant.get("puuid", "0")
    #     participant_details = riot_api.get_Summoner(value=participant_puuid, by="puuid")
    #     participant["player_name"] = participant_details.get("name")
    #     participant["player_details"] = participant_details
    print(match)
