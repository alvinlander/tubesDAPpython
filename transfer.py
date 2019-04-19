import json
import simpan
import menutf
import usertujuan
import riwayattflainnya
import getpass
import os
def transfer():
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
            m = menutf.menu()
            if m == 1:
                usertujuan.user()
                g = open("usersesama.txt", "r+")
                h = json.load(g)
                i = 0
                ketemu = False
                while i < len(d) and not ketemu:
                    if d[i][1] == h[0]:
                        ketemu = True
                    else:
                        i = i + 1
                    if ketemu == True:
                        print("Jumlah Transfer: ", end="")
                        y = int(input())
                        cek = 0
                        while cek == 0:
                            u = getpass.getpass('Masukkan PIN : ')
                            if u != d[f][3]:
                                print("PIN SALAH")
                                input()
                            else:
                                cek = cek + 1
                        if y <= d[f][2]:
                            hasil = d[f][2] - y
                            d[f][2] = hasil
                            simpan.Simpan(d)
                            hasil = d[i][2] + y
                            d[i][2] = hasil
                            simpan.Simpan(d)
                    else:
                        hasil = ketemu
            elif m == 2:
                print("Username Tujuan: ", end="")
                s = input()
                print("Jumlah Transfer : ", end="")
                t = int(input(""))
                L = [s,t]
                cek = 0
                while cek == 0:
                    u = getpass.getpass('Masukkan PIN : ')
                    if u != d[f][3]:
                        print("PIN SALAH")
                        input()
                    else:
                        cek = cek + 1
                if t >= 50000 :
                    hasil = d[f][2] - t
                    d[f][2] = hasil
                    simpan.Simpan(d)
                    riwayattflainnya.tflain(L)
                else:
                    print("Saldo tidak cukup")
                    input()
        else:
            hasil = nemu



