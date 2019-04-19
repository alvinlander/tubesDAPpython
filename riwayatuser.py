import json
def user(b):
    a = open("riwayat user.txt", "w")
    b = json.dump(b, a)