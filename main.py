from riot_api.lol import lol


if __name__ == '__main__':
    key = "RGAPI-a52fab9e-1da5-43a1-b3f0-c702c938ffdd"
    by = "id"
    val = "svMEdXMIn49ZJskKIXlKO91EMn9I0-qsfTWjGzaPF3k5rNpU"
    RiotApi = lol(key)
    response = RiotApi.get_Summoner(val,by)
    print(response)