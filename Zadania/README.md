**BIG DIAGNOZA Python**
- [Księga 1: Skrypty Algorytmy](#księga-1-skrypty-algorytmy)
- [Księga 2: Zadania](#księga-2-zadania)
  - [Diagnoza INF](#diagnoza-inf)
    - [Wstęp](#wstęp)
      - [Zadanie 1 - Oblicz sumę liczb 3-cyfrowych](#zadanie-1---oblicz-sumę-liczb-3-cyfrowych)
      - [Zadanie 2 - Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6](#zadanie-2---oblicz-sumę-i-ilość-dwucyfrowych-wielokrotności-liczby-6)
      - [Zadanie 3 - Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych](#zadanie-3---znajdź-największą-liczbę-wśród-5-wylosowanych-przez-program-liczb-4-cyfrowych)
      - [Zadanie 4 - Podaj sumę cyfr w dowolnej liczbie](#zadanie-4---podaj-sumę-cyfr-w-dowolnej-liczbie)
      - [Zadanie 5 - Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej](#zadanie-5---znajdź-najmniejszą-cyfrę-we-wpisanej-przez-usera-liczbie-3-cyfrowej)
    - [Algorytmy](#algorytmy)
      - [Zadanie 1 - Sprawdź czy wpisana przez usera liczba jest pierwsza](#zadanie-1---sprawdź-czy-wpisana-przez-usera-liczba-jest-pierwsza)
      - [Zadanie 2 - Sprawdź czy wpisana przez usera liczba jest złożona](#zadanie-2---sprawdź-czy-wpisana-przez-usera-liczba-jest-złożona)
      - [Zadanie 3 - Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24](#zadanie-3---sprawdź-czy-wpisana-przez-usera-liczba-jest-względnie-pierwsza-z-24)
      - [Zadanie 4 - Zakoduj szyfrem CEZARA i kluczem k słowo s](#zadanie-4---zakoduj-szyfrem-cezara-i-kluczem-k-słowo-s)
      - [Zadanie 5 - Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbe mieszaną](#zadanie-5---dodaj-dwa-ułamki-ab--cd-zapisz-sumę-jako-ułamek-nieskracalny-i-liczbe-mieszaną)
      - [Zadanie 6 - Znajdź NWW dwóch wpisanych przez usera liczb](#zadanie-6---znajdź-nww-dwóch-wpisanych-przez-usera-liczb)
    - [Kartka](#kartka)
      - [Zadanie 1 - Oblicz wartość ONP](#zadanie-1---oblicz-wartość-onp)
        - [Przykład](#przykład)
      - [Zadanie 2 - Znajdź postać ONP do piemnego wyrażenia](#zadanie-2---znajdź-postać-onp-do-piemnego-wyrażenia)
        - [Przykład](#przykład-1)
      - [Zadanie 3 - Napisz na kartce algorytm NWD (obie wersje) i przeprowadź symulacje kroków dla podanych liczb](#zadanie-3---napisz-na-kartce-algorytm-nwd-obie-wersje-i-przeprowadź-symulacje-kroków-dla-podanych-liczb)
        - [Przykład](#przykład-2)
    - [Napisy](#napisy)
      - [Zadanie 1 - Znajdź ilość liter C we wpisanym napisie](#zadanie-1---znajdź-ilość-liter-c-we-wpisanym-napisie)
      - [Zadanie 2 - Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA](#zadanie-2---sprawdź-czy-literki-w-napisie-są-w-porządku-nierosnącym-np-zoo-wok-woda)
      - [Zadanie 3  - Podaj najdłuższy z 3 wpisanych przez usera wyrazów.](#zadanie-3----podaj-najdłuższy-z-3-wpisanych-przez-usera-wyrazów)


# [Księga 1: Skrypty Algorytmy](https://github.com/Pawi1/BIG-DIAGNOZA-Python/edit/main/Skrypty-Algorytmy)
# Księga 2: Zadania
## Diagnoza INF
### Wstęp
#### Zadanie 1 - Oblicz sumę liczb 3-cyfrowych
```python
e1,e2,e3 = int(input("1. 1: ")),int(input("1. 2: ")),int(input("1. 3: "))
suma = e1 + e2 + e3
print(suma) 
# We: 10,80,12
# Wy: 102
```
#### Zadanie 2 - Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
```python
suma,ilosc = 0,0
for i in range(6,100,6):
    if i>9 and i<100:
        ilosc += 1
        suma += i
print(suma,ilosc)
```
#### Zadanie 3 - Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
```python
import random
A = []
for i in range(5):
    A.append(random.randint(1000,9999))
maks = A[0]
for i in A:
    if i > maks:
        maks = i
print(maks)
```
#### Zadanie 4 - Podaj sumę cyfr w dowolnej liczbie
```python
zad4_e = int(input("4. Podaj dowolną cyfre: "))
zad4_sum = 0
for i in str(zad4_e):
    zad4_sum += int(i)
print(zad4_sum)
# We : 523
# Wy : 10
```
#### Zadanie 5 - Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
```python
zad5_e = int(input("5. Podaj 3-cyfrową liczbe: "))
mini = 10
for i in str(zad5_e):
    i = int(i)
    if i < mini:
        mini = i
print(mini)
# We : 523
# Wy : 2
```
### Algorytmy
#### Zadanie 1 - Sprawdź czy wpisana przez usera liczba jest pierwsza
```python
n = int(input("1. Podaj liczbe: "))
n = 420
boolCzyPierwsza = True
for i in range(2,n):
    if n % i == 0:
         boolCzyPierwsza = False
print(boolCzyPierwsza)
# We : 420
# Wy : False
```
#### Zadanie 2 - Sprawdź czy wpisana przez usera liczba jest złożona
```python
n = int(input("1. Podaj liczbe: "))
n = 420
boolCzyPierwsza = False
for i in range(2,n):
    if n % i == 0:
         boolCzyPierwsza = True
print(boolCzyPierwsza)
# We : 420
# Wy : True
```
#### Zadanie 3 - Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
```python
n = int(input("3. Podaj liczbe: "))
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a
if 1 == nwd(n,24):
    print(True)
else:
    print(False)
# We : 420
# Wy : False
```
#### Zadanie 4 - Zakoduj szyfrem CEZARA i kluczem k słowo s
```python
def cesar(napis,k):
    szyfr = ""
    for i in range(len(napis)):
        szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + k) % 26)
    return szyfr
s = input("4. s: ")
k = input("4. k: ")
print(cesar(s,k))
# We : KochamInformatyke , 3
# Wy : NXLQJVLWOXAVJCHTN
```
#### Zadanie 5 - Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbe mieszaną
```python
def nww(a,b):    
    iloczyn = a * b
    while b > 0:
         a, b = b, a % b
    return (iloczyn//a)
def ulamkiDodawanie(a,b,c,d,bo):
    if bo == True:print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)}/{nww(b,d)} = {((nww(b,d)//b*a)+(nww(b,d)//d*c))/(nww(b,d))} ")
    return str((nww(b,d)//b*a)+(nww(b,d)//d*c))+"/"+ str((nww(b,d)))


def ulamkiMieszane(a_przez_b):
    a = int(a_przez_b[0])
    b = int(a_przez_b[2])
    if a%b != 0:
        return str(a//b) +" "+ str(a%b)+"/"+str(b) 
    else: 
        return str(a)+"/"+str(b)
    
def ulamkiSkracanie(a_przez_b):
    a = int(a_przez_b[0])
    b = int(a_przez_b[2])
    return str(a//nwd(a,b))+"/"+str(b//nwd(a,b))

a = input("5. a: ")
b = input("5. b: ")
c = input("5. c: ")
d = input("5. d: ")
print(ulamkiSkracanie(ulamkiDodawanie(a,b,c,d,True)))
print(ulamkiMieszane(ulamkiDodawanie(a,b,c,d,False)))

# We : 1,1,4,4
# Wy : 1/1 + 4/4 = 4/4 + 4/4 = 8/4 = 2.0 
#      2/1
#      8/4
```
#### Zadanie 6 - Znajdź NWW dwóch wpisanych przez usera liczb
```python
def nww(a,b):    
    iloczyn = a * b
    while b > 0:
         a, b = b, a % b
    return (iloczyn//a)
a = input("6. a: ")
b = input("6. b: ")
print(nww(a,b))
# We : 6,9
# Wy : 18
```
### Kartka
#### Zadanie 1 - Oblicz wartość ONP
##### Przykład
```
ONP: 2 3 5 - 3 * -
Notacja z nawiasami:  2 - (3 - 5) * 3 
Wynik: 8
``` 
#### Zadanie 2 - Znajdź postać ONP do piemnego wyrażenia
##### Przykład
```
ONP: 428-*
Notacja z nawiasami: 4*(2-8)
```
#### Zadanie 3 - Napisz na kartce algorytm NWD (obie wersje) i przeprowadź symulacje kroków dla podanych liczb
```python
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a

def nwd_o(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```
##### Przykład
```
10 ~~ 6
 4 || 6
 4 || 2
 2 || 2
NWD = 2

15 ~~ 5
10 || 5
 5 || 5
NWD = 5
```
### Napisy
#### Zadanie 1 - Znajdź ilość liter C we wpisanym napisie
```python
napis = input("1. Podaj napis: ")
ilosc = 0
for i in range(len(napis)):
    if napis[i] == "C":
        ilosc += 1
print(ilosc)
# We : CECYLIA
# Wy : 2
```
#### Zadanie 2 - Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA
```python
wejscie = input("2. Podaj napis: ")
def ciagMalejaccy(wejscie):
    alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]
    flaga = True
    for i in range(len(wejscie)-1):
        if alfabet.index(wejscie[i]) < alfabet.index(wejscie[i+1]):
            flaga = False
    return flaga
print(ciagMalejaccy(wejscie))
# We : ZOO
# Wy : True
```
#### Zadanie 3  - Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
```python
napis1,napis2,napis3 = input("3. 1: "),input("3. 2: "),input("3. 3: ")
if napis1 > napis2 and napis1 > napis3: print("1")
if napis2 > napis1 and napis2 > napis3: print("2")
if napis3 > napis2 and napis3 > napis1: print("3")
# We : LOLEK , BOLEK , TROLEK
# Wy : 3
```
