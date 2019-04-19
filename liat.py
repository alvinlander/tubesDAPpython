def viewAll(b):
    print("Nama Lengkap\tUsername\tSaldo\tPin\tWaktu")
    for x in range(len(b)):
	    print('%s\t%s\t\t%s\t%s\t%s' %(b[x][0],b[x][1],b[x][2],b[x][3],b[x][4]))
