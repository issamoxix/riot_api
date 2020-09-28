import summ , sys
data_ = summ.argparser()
data = vars(data_)
Summoner = summ.summoner(data['u'],data['r'],data['k'])
Summoner.res()