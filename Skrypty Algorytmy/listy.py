
#* Usuń z listy wszystkie liczby x
def usunLiczbe(K,x):
    for i in range(K.count(x)):
        K.pop(K.index(x))
    return K
#* Szukaj maxa w liscie
def maxWliscie(K):
    maks = K[0]
    for i in K:
        if i > maks:
            maks = i
    return maks
#* Szukaj mini w liście
def miniWliscie(K):
    mini = maxWliscie(K)
    for i in K:
        if i < mini:
            mini = i
    return mini