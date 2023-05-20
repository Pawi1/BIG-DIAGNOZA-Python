# BIG DIAGNOZA Python
### [Rozdział 1: Algorytmy](#rozdział-1:-algorytmy)
### [Rozdział 2: Szyfrowanie](#rozdział-2:-szyfrowanie)
### [Rozdział 3: Listy](rozdział-3:-listy)
## Rozdział 1: Algorytmy

### NWD
### Biblioteka
```python
from math import gcd 
gcd(x,y)
```
### Algorytm
```python
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a
```
### NWW
Wersja 1 - Bez NWD
```python
def nww(a,b):    
    iloczyn = a * b
    while b > 0:
         a, b = b, a % b
    return (iloczyn//a)
```
Wersja 2 - Z NWD
```python
def nww(a,b):    
    return (a*b//nwd(a,b))
```
### Pierwsze
```python
 def czyPierwsza(n):
     boolCzyPierwsza = True
     for i in range(2, n):
         if n % i == 0:
             boolCzyPierwsza = False
     return boolCzyPierwsza
```
### Ułamki - Dodawanie
```python
def ulamkiDodawanie(a,b,c,d):
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)/{nww(b,d)} }")
    return (nww(b,d)//b*a)+(nww(b,d)//d*c)/nww(b,d)
```
### Ułamki - Odejmowanie
```python
def ulamkiUdejmowanie(a,b,c,d):
    print(f"{a}/{b} - {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} - {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)-(nww(b,d)//d*c)/{nww(b,d)} }")
    return (nww(b,d)//b*a)+(nww(b,d)//d*c)/nww(b,d)
```
### Reszta
Wersja 1 - Lista
```python
x = int(input())
T = [50,20,10,5,2,1]
W = []
for i in T:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        for j in range(ilosc):
            W.append(i)
print(W)
```
Wersja 2
```python
x = int(input())
T = [50,20,10,5,2,1]
for i in T:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        print(f"Nominał {i} ilość {ilosc}")
```

## Rozdział 2: Szyfrowanie
### Cesar
```python
def cesar(napis):
    szyfr = ""
    for i in range(len(napis)):
        szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + 3) % 26)
    return szyfr
```
### Hufman
```python
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
```
### RSA
```python
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
```
## Rozdział 3: Napisy
### Sortowanie stringa - String -> Lista -> String
```python
def sortowanieStringa(s):
    L = list(s)
    L.sort()
    w = "".join(L)
    return w
```
### Palindrom
```python
def czyPalindrom(s):
    L,R = list(s),list(s)
    R.reverse()
    if L == R:
        return True
    else:
        return False
```
### Anagram
```python
def czyAnagram(a,b):
    X, Y = list(a), list(b)
    X.sort()
    Y.sort()
    a, b = "".join(X), "".join(Y)
    if a == b:
        return True
    else:
        return False
```
## Rozdział 3: Listy
### Usuń wszystkie liczby x z listy
```python
def usunLiczbe(K,x):
    for i in range(K.count(x)):
        K.pop(K.index(x))
    return K
```
### Szukaj liczby największej w liście
```python
def maxWliscie(K):
    maks = K[0]
    for i in K:
        if i > maks:
            maks = i
    return maks
```
### Szukaj liczby najminiejszej w liście
```python
def miniWliscie(K):
    mini = maxWliscie(K)
    for i in K:
        if i < mini:
            mini = i
    return mini
```
