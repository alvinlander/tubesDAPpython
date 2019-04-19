import json
import header
import inputuser
import os
def loginuser():
    os.system("cls")
    x = open('nasabah.txt', 'r+')
    y = json.load(x)
    header.header()
    z = inputuser.user()
    os.system("cls")
    pos = 0
    f = False
    while pos < len(y) and not f :
        if y[pos][1] == z :
            f = True
        else :
            pos = pos + 1
        if f == True:
            hasil = y[pos][1]
        else:
            hasil = f
    return hasil
