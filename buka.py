import json
def Open():
    x = open('nasabah.txt','r+')
    return json.load(x)
