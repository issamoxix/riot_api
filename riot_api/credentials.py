class credentials:
    key: str
    username: str

    def __init__(self, key, region="euw1", game="lol"):
        self.key = key
        self.region = region
        self.game = game

    def CheckKey(self):
        print(self.key)

    def getUrl(self, api_type):
        self.url = f"https://{self.region}.api.riotgames.com/{self.game}/{api_type}?api_key={self.key}"
        return self.url
