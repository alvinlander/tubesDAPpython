u = input('Username = ')
import getpass
p = getpass.getpass("Password:")
if p == 'mimin' and u == 'admin':
    print('login sukses')
else :
    print('salah')
    
