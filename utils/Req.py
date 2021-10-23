import requests 

def getReq(url):
    req = requests.get(url)
    return req.json()