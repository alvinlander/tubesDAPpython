import json
import simpan
def penarikan():
    a = open("riwayat user.txt", "r+")
    b = json.load(a)
    c = open("nasabah.txt", "r+")
    d = json.load(c)
    f = 0
    nemu = False
    while f < len(d) and not nemu:
        if d[f][1] == b[0] :
            nemu = True
        else:
            f = f + 1
        if nemu == True :
            print("Nominal : ", end="")
            t = int(input(""))
            if t >= 50000 and t <= d[f][2]:
                hasil = d[f][2] - t
                d[f][2] = hasil
                simpan.Simpan(d)
            else:
                print("Saldo tidak cukup")
                input()
        else:
            hasil = nemu