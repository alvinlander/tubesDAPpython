import liatuser
import header
import ceksaldo
import tampilanuser
import transfer
import penarikan
import setoran
import os
def menu():
    os.system('cls')
    header.header()
    x = tampilanuser.ui()
    os.system('cls')
    while x != 5 :
        header.header()
        if x == 1:
            o = liatuser.search()
            L = []
            L.append(o)
            ceksaldo.saldo(o)
            print("Tekan Enter untuk kembali")
            input()
        elif x == 2:
            transfer.transfer()
            print("Tekan Enter untuk kembali")
            input()
        elif x == 3:
            penarikan.penarikan()
            print("Tekan Enter untuk kembali")
            input()
        elif x == 4:
            setoran.setoran()
            print("Tekan Enter untuk kembali")
            input()
        elif x == 5:
            tutupprogram.tutup()
        os.system('cls')
        header.header()
        x = tampilanuser.ui()
        os.system('cls')
            
