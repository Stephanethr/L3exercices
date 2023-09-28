def modif_lst(L1, L2):
    res = []
    if len(L1) != 0:
        L1[0] = 1000
    L2 = L1
    res = L1
    L1 = []
    return res


L = [0, 1, 2, 3, 4, 5]
P = [2, 3]
print("avant appel L= ", str(L))
print("avant appel P= ", str(P))
R = modif_lst(L, P)
print("après appel L= ", str(L))
print("après appel P= ", str(P))
print("R = ", str(R))
