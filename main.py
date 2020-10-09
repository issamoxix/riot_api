import summ , sys
# data_ = summ.argparser()
# data = vars(data_)
# Summoner = summ.summoner(data['u'],data['r'],data['k'])
# Summoner.res()
# print(Summoner.accountId)
league_api = summ.summoner('Summoner name','euw','api_key')

solo_q=league_api.rank_data
league_api.res()