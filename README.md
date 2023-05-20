# BIG DIAGNOZA Python
## Rozdział 1: Algorytmy

### NWD - Euklides
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
### Ułamki Dodawanie
```python
def ulamkiDodawanie(a,b,c,d):
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)/{nww(b,d)} }")
    return (nww(b,d)//b*a)+(nww(b,d)//d*c)/nww(b,d)
```
### Ułamki Odejmowanie
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

```