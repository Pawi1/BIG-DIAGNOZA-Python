
#* Cesar    
def cesar(napis):
    szyfr = ""
    for i in range(len(napis)):
        szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + 3) % 26)
    return szyfr

#* Hufman
def hufman(W):
    H = ""
    ilosc = 1
    for i in range(len(W)-1):
        if W[i] == W[i+1]:
            ilosc += 1
        else:
            if ilosc > 1:
                H += str(ilosc)
            H += W[i]
            ilosc = 1
    if ilosc > 1:
        H += str(ilosc)
    H += W[len(W)-1]
    return H

#* RSA
e,d = 0,0
# 1. Wybór 2 dużych liczb pierwszych
p = 11
q = 13
print(p,q)
# 2. Stworzenie funkcji Eulera F = (p-1) * (q-1) i znalezienie n = p*q
F = (p - 1) * (q - 1)
n = p * q
print(n)
print(F)

# 3. Wygenerowanie klucza publicznego e: NWD(F,e) = 1
from math import gcd
for i in range(2,F):
    if gcd(i,F) == 1:
        e = i
        break
print(e,n)

# 4. Wygenerowanie klucza prywatnego d: d*e mod F = 1 (odwrotność modulo)
for i in range(2,F):
    if (i*e) % F == 1:
        d = i
        break
print(d,n)

# Przykład działania kodowania znaku x:
# c = x**e mod n (na szyfrogram)
# t = c**d mod n (na tekst jawny)

msg = input()
szyfrogram = ""
for i in msg:
    szyfrogram += chr((ord(i)**e) % n)
print(szyfrogram)

jawny = ""
for j in szyfrogram:
    jawny += chr((ord(j)**d) % n)
print(jawny)