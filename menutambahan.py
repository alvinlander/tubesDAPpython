import buka
import hapus
import liat
import simpan
import nabanala
import tampilan
import header
import inputdata
import tutupprogram
import json
import os
import mainlogin
import userpw
def menu2():
    header.header
    nabanala.naba()
    y =int(input("Masukkan Pilihan : "))
    if (y == 1) :
        L = []
    elif (y==2) :
        L = buka.Open()
    os.system('cls')
    header.header()
    pil = tampilan.tapil()
    os.system('cls')
    while pil != 6 :
        header.header()
        if pil == 1 :
            L = inputdata.tambah(L)
            print("enter untuk kembali ke menu")
            input()
        elif (pil==2):
            L = hapus.Hapus(L)
            print("Data berhasil dihapus, enter untuk kembali menu")
            input()
        elif (pil==3):
            liat.viewAll(L)
            print("enter untuk kembali ke menu")
            input()
        elif (pil==4):
            simpan.Simpan(L)
            print("Data berhasil di simpan, enter untuk kembali ke menu")
            input()
        elif (pil==5):
            tutupprogram.tutup()
        os.system('cls')
        header.header()
        pil = tampilan.tapil()
        os.system('cls')
