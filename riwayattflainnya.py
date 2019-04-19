import json
def tflain(b):
    a = open("riwayatTFlain.txt", "w")
    b = json.dump(b, a)