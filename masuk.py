import userlogin
import header
import os
def masukuser():
    cek = 0
    while cek == 0:
        header.header()
        a = userlogin.loginuser()
        if a == False:
            print("Username tidak dikenal")
            input()
        else :
            cek = cek + 1
        os.system('cls')
