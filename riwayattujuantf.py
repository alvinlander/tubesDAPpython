import json
def tujuan(b):
    a = open("usersesama.txt", "w")
    b = json.dump(b, a)