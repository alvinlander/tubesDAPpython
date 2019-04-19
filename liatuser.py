import json
import json
def search():
    x = open('nasabah.txt', 'r+')
    n = json.load(x)
    y = open('riwayat user.txt', 'r+')
    m = json.load(y)
    f = 0
    nemu = False
    while f < len(n) and not nemu:
        if n[f][1] == m[0] :
            nemu = True
        else:
            f = f + 1
        if nemu == True :
            hasil = n[f][0],n[f][2]
        else:
            hasil = nemu
    return hasil



