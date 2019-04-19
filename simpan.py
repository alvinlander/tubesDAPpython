import json
def Simpan(b):
    a = open('nasabah.txt','w')
    b = json.dump(b,a)
