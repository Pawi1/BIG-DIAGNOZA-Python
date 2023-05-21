 #* NWD - Euklides
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a

#* NWW
def nww(a,b):    
    iloczyn = a * b
    while b > 0:
         a, b = b, a % b
    return (iloczyn//a)

#? Alternatywny zapis jeżeli już wcześniej zadeklarowaliśmy NWD
def nwwAlt(a,b):    
    return (a*b//nwd(a,b))
#* Pierwsze
def czyPierwsza(n):
    boolCzyPierwsza = True
    for i in range(2, n):
        if n % i == 0:
            boolCzyPierwsza = False
    return boolCzyPierwsza

#* Ułamki
# Dodawanie
def ulamkiDodawanie(a,b,c,d):
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)+(nww(b,d)//d*c))+"/"+ str((nww(b,d)))
# Odejmowanie
def ulamkiUdejmowanie(a,b,c,d):
    print(f"{a}/{b} - {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} - {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)-(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)-(nww(b,d)//d*c))+"/"+ str((nww(b,d)))

#* Reszta
#? Wersja 1 - Lista
def reszta(T,x):
    W = []
    for i in T:
        ilosc = x // i
        if ilosc > 0:
            x = x - ilosc * i
            for j in range(ilosc):
                W.append(i)
    return W
#? Wersja 2 - Print
x = int(input())
T = [50,20,10,5,2,1]
for i in T:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        print(f"Nominał {i} ilość {ilosc}")
#* Dziel i Zwyciężaj - szukanie mini i maksi z listy
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
#* ONP - liczenie
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
