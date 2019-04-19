import riwayatuser
def user():
    print("Username: ", end="")
    a = input()
    L = []
    L.append(a)
    riwayatuser.user(L)
    return a