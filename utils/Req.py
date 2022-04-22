import requests


def getReq(url, key, optional_kwargs={}):
    params = {"key": key} | optional_kwargs
    req = requests.get(url, params=params)
    return req.json()
