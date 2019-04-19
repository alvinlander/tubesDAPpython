import os
import header
import mainlogin
import userpw
import menutambahan
import masuk
import tampilanuser
import menu1
os.system('cls')
header.header()
mainlogin.pilog()
x = int(input("Masukkan pilihan : "))
os.system('cls')
if x == 1:
    userpw.akunadmin()
    os.system('cls')
    header.header()
    os.system('cls')
    menutambahan.menu2()
    
elif x == 2 :
    header.header()
    masuk.masukuser()
    os.system('cls')
    menu1.menu()
