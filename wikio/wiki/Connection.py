import json

try: # This allows to adapt to the Python's version
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

class connection:

    __instance = None

    @staticmethod
    def getInstance():
        if connection.__instance == None:
            connection()
        return connection.__instance


    def __init__(self):
        if connection.__instance != None :
            raise Exception("Singleton error!")
        else :
            connection.__instance = self

    def get(self, action, value):
        url = "https://en.wikipedia.org/w/api.php?action=query"

        if action == "search":
            url += "&list=search&srsearch="+value.replace(" ","%20")
        elif action == "getbyId":
            #url += "&prop=revisions&rvprop=content&pageids="+value
            url += "&prop=extracts&exintro=&explaintext=&pageids="+str(value)

        url += "&format=json&utf8="

        return json.load(urlopen(url))

    def find(ids):
        url = "https://en.wikipedia.org/w/api.php?action=query"

        url += "&prop=extracts&exintro=&explaintext=&pageids="+str(value)

        url += "&format=json&utf8="

        return json.load(urlopen(url))["query"]["pages"][str(ids)]["title"]
