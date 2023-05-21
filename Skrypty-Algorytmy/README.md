**BIG DIAGNOZA Python**

- [Księga 1: Skrypty, Algorytmy](#księga-1-skrypty-algorytmy)
  - [Rozdział 1: Algorytmy](#rozdział-1-algorytmy)
    - [NWD](#nwd)
      - [Biblioteka](#biblioteka)
      - [Algorytm](#algorytm)
    - [NWW](#nww)
    - [Pierwsze](#pierwsze)
    - [Ułamki - Dodawanie](#ułamki---dodawanie)
    - [Ułamki - Odejmowanie](#ułamki---odejmowanie)
    - [Zachłanne - wydawanie reszty](#zachłanne---wydawanie-reszty)
      - [Wersja 1 - Lista](#wersja-1---lista)
      - [Wersja 2 - Print](#wersja-2---print)
    - [Dziel i Zwyciężaj - szukanie mini i maksi z listy](#dziel-i-zwyciężaj---szukanie-mini-i-maksi-z-listy)
    - [ONP](#onp)
  - [Rozdział 2: Szyfrowanie](#rozdział-2-szyfrowanie)
    - [Cesar](#cesar)
    - [Hufman](#hufman)
    - [RSA](#rsa)
  - [Rozdział 3: Napisy](#rozdział-3-napisy)
    - [Sortowanie stringa - String -\> Lista -\> String](#sortowanie-stringa---string---lista---string)
    - [Palindrom](#palindrom)
    - [Anagram](#anagram)
  - [Rozdział 3: Listy](#rozdział-3-listy)
    - [Usuń wszystkie liczby x z listy](#usuń-wszystkie-liczby-x-z-listy)
    - [Szukaj liczby największej w liście](#szukaj-liczby-największej-w-liście)
    - [Szukaj liczby najminiejszej w liście](#szukaj-liczby-najminiejszej-w-liście)
  - [Rozdział 4: Sortowanie](#rozdział-4-sortowanie)
    - [Sortowanie Szybkie](#sortowanie-szybkie)
      - [Hoare](#hoare)
      - [Lomuto](#lomuto)
    - [Sortowanie poprzez wstawianie](#sortowanie-poprzez-wstawianie)
    - [Sortowanie bąbelkowe](#sortowanie-bąbelkowe)
    - [Sortowanie poprzez zliczanie](#sortowanie-poprzez-zliczanie)
    - [Sortowanie poprzez wybieranie](#sortowanie-poprzez-wybieranie)
- [Księga 2: Zadania](#księga-2-zadania)
# Księga 1: Skrypty, Algorytmy 
## Rozdział 1: Algorytmy
### NWD
#### Biblioteka
```python
from math import gcd 
gcd(x,y)
```
#### Algorytm
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
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)+(nww(b,d)//d*c))+"/"+ str((nww(b,d)))
```
### Ułamki - Odejmowanie
```python
def ulamkiUdejmowanie(a,b,c,d):
    print(f"{a}/{b} - {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} - {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)-(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)-(nww(b,d)//d*c))+"/"+ str((nww(b,d)))
```
### Zachłanne - wydawanie reszty
#### Wersja 1 - Lista
```python
def reszta(T,x):
    W = []
    for i in T:
        ilosc = x // i
        if ilosc > 0:
            x = x - ilosc * i
            for j in range(ilosc):
                W.append(i)
    return W
```
#### Wersja 2 - Print
```python
def reszta(T,x):
    for i in T:
        ilosc = x // i
        if ilosc > 0:
            x = x - ilosc * i
            print(f"Nominał {i} ilość {ilosc}")
    return 0
```
### Dziel i Zwyciężaj - szukanie mini i maksi z listy
```python
def dzielZwyciężaj(T):
    n = len(T)
    if n%2==1:
        dl = n-2
    else:
        dl = n-1 
    if T[0]<T[1]:
        mini = T[0]
        maxi = T[1]
    else:
        mini = T[1]
        maxi = T[0]
    i = 2
    while i<dl:
        if T[i]<T[i+1]:
            if T[i]<mini:
                mini = T[i]
            if T[i+1]>maxi:
                maxi = T[i+1]
        else:
            if T[i+1]<mini:
                mini = T[i+1]
            if T[i]>maxi:
                maxi = T[i]
        i+=2

    if n%2==1:
        if T[n-1]<mini:
            mini = T[n-1]
        if T[n-1]>maxi:
            maxi=T[n-1]

    return [mini, maxi]
```
### ONP
```python
def onp(E):
    R = []
    for i in E:
        if i.isdigit():
            R.append(i)
        else:
            if i == "+":
                x = int(R[len(R)-2]) + int(R[len(R)-1])
                R.pop()
                R.pop()
                R.append(x)
            if i == "-":
                x = int(R[len(R)-2]) - int(R[len(R)-1])
                R.pop()
                R.pop()
                R.append(x)
            if i == "*":
                x = int(R[len(R)-2]) * int(R[len(R)-1])
                R.pop()
                R.pop()
                R.append(x)
            if i == "/":
                x = int(R[len(R)-2]) // int(R[len(R)-1])
                R.pop()
                R.pop()
                R.append(x)
    return R[0]
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
## Rozdział 4: Sortowanie
### Sortowanie Szybkie 
#### Hoare
```python
def quicksortHoare(T, lewy, prawy):
    i = lewy
    j = prawy
    pivot = T[(lewy+prawy)//2]

    while i <= j:
        while T[i] < pivot:
            i = i + 1
        while T[j] > pivot:
            j = j - 1
        if i <= j:
            T[i], T[j] = T[j], T[i]
            i = i + 1
            j = j - 1
    
    if lewy < j:
        quicksortHoare(T, lewy, j)
    if prawy > i:
        quicksortHoare(T, i, prawy)
```
#### Lomuto
```python
def quicksortLomuto(T, lewy, prawy):
    pivot = T[prawy]
    i = lewy
    for k in range(lewy, prawy):
        if T[k] <= pivot:
            T[i], T[k] = T[k], T[i]
            i = i + 1
    
    T[i], T[prawy] = T[prawy], T[i]

    if lewy<i-1:
        quicksortLomuto(T, lewy, i-1)
    if prawy>i+1:
        quicksortLomuto(T, i+1, prawy)
```
### Sortowanie poprzez wstawianie
```python
def insertionSort(A):
    if (n := len(A)) <= 1:
      return
    for i in range(1, n):
        key = A[i]
        j = i-1from random import randint
T = [randint(1,30) for i in range(9)]
print(T)
print(dzielZwyciężaj(T))
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
```
### Sortowanie bąbelkowe
```python
def bubbleSort(T):
    n = len(T)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if T[i] > T[i+1]:
                T[i], T[i+1] = T[i+1], T[i]
```
### Sortowanie poprzez zliczanie
```python
def countingSort(T, m):
    P = []
    for i in range(m):
        P.append(0)
    for i in T:
        P[i] += 1
    k = 0
    for i in range(m):
        for j in range(0, P[i]):
            T[k] = i
            k += 1
```
### Sortowanie poprzez wybieranie
```python
def selectionSort(T):
    n = len(T)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if T[j] < T[k]:
                k = j
        T[k], T[i] = T[i], T[k]
```
# [Księga 2: Zadania](https://github.com/Pawi1/BIG-DIAGNOZA-Python/edit/main/Zadania)