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
```python
def nww(a,b):    
    iloczyn = a * b
    while b > 0:
         a, b = b, a % b
    return (iloczyn//a)
```
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
### Ułamki
```python
a,b,c,d = int(input()), int(input()), int(input()), int(input())

x = b
y = d
iloczyn = x*y
while y>0:
    x, y = y, x%y
nww = iloczyn // x

e = (nww // b) * a
f = (nww // d) * c
g = e + f

print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")
```
