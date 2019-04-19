import os
import header
import json
import waktu
os.system("cls")
def tambah(L):
   a = "ya"
   while a == "ya" :
      print("Masukkan Nama Lengkap\t\t: ", end="")
      x = input()
      if len(x) <= 16 :
         break
      else:
         print()
         a = input("Maksimal Nama 16 Karakter. Masukkan lagi? ya/tidak")
         print()
   b = "ya"
   while b == "ya":
      print("Masukkan Username\t\t: ", end="")
      p = input()
      if len(p) <= 10:
         break
      else:
         print()
         b = input("Maksimak Username 10 karakter. Masukkan lagi?ya/tidak")
         print()
   c = "ya"
   while c == "ya":
      print("Masukkan Setoran Awal(Min. 500000)\t\t: ", end="")
      y = int(input())
      if y >= 500000 :
         break
      else:
         print()
         a = input("Setoran dibawah jumlah minimum. Masukkan lagi ? ya/tidak")
         print()
   e = "ya"
   while e =="ya":
       print("Masukkan PIN anda (6 Digits)\t\t: ", end="")
       z = input()
       if len(z) == 6 :
           break
       else:
           print()
           a = input("PIN tidak sesuai ketentuan. Masukkan lagi? ya/tidak")
           print()
   import json
   o = waktu.waktu()
   print(o)
   os.system("cls")
   header.header()
   os.system("cls")
   p = [x,p,y, z, o]
   L.append(p)
   return L




