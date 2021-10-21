
class credentials:
    key:str
    username:str
    def __init__(self,key,username):
        self.key = key
        self.username = username
    def CheckKey(self):
        print(self.key)