import requests
import json
import os
from pprint import pprint
def run(name, key):
	r = requests.get("https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+key)
	fx = open(name+'.json', 'x')
	fx.write(r.text)
	fx.close()
	with open(name+'.json') as f:
		info = json.load(f)
	lvl  = json.dumps(info['summonerLevel'])
	sumid = json.dumps(info['id'])
	ra = requests.get("https://euw1.api.riotgames.com/lol/league/v3/positions/by-summoner/"+sumid+"?api_key="+key)
	fy = open(name+'1.json','x')
	fy.write(ra.text)
	fy.close()
	with open(name+'1.json') as d:
		info1 = json.load(d)
	# pprint(info1)
	rank = json.dumps(info1[0]['rank'])
	tier = json.dumps(info1[0]['tier'])
	print('Your lvl: '+lvl+'\nSummoner Id: '+sumid+'\n===>'+tier+rank+'<===')
	os.remove(name+'1.json')
	os.remove(name+'.json')
