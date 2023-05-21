
#! - WSTĘP

#* 1. Olicz sume liczb 3-cyfrowych
# zad1_e1,zad1_e2,zad1_e3 = int(input("1. Wprowadź liczbe 1/3 liczbe: ")),int(input("1. Wprowadź 2/3 liczbe: ")),int(input("1. Wprowadź liczbe 3/3 liczbe: "))
zad1_e1,zad1_e2,zad1_e3 = 10,80,12
zad1_sum = zad1_e1 + zad1_e2 + zad1_e3
print(zad1_sum)

#* 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
zad2_sum,zad2_ilosc = 0,0
for i in range(6,100,6):
    if i>9 and i<100:
        zad2_ilosc += 1
        zad2_sum += i
print(zad2_sum,zad2_ilosc)

#* 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
import random
zad3_A = []
for i in range(5):
    zad3_A.append(random.randint(1000,9999))
maks = zad3_A[0]
for i in zad3_A:
    if i > maks:
        maks = i
print(maks)

#* 4. Suma cyfr w dowolnej liczbie
# zad4_e = int(input("4. Podaj dowolną cyfre: "))
zad4_e = 523
zad4_sum = 0
for i in str(zad4_e):
    zad4_sum += int(i)
print(zad4_sum)

#* 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# zad5_e = int(input("5. Podaj 3-cyfrową liczbe: "))
zad5_e = 523
mini = 10
for i in str(zad5_e):
    i = int(i)
    if i < mini:
        mini = i
print(mini)

#! Algorytmy

#* 1. Czy liczba usera jest pierwsza
# n = int(input("1. Podaj liczbe: "))
n = 420
boolCzyPierwsza = True
for i in range(2,n):
    if n % i == 0:
         boolCzyPierwsza = False
print(boolCzyPierwsza)

#* 2. Czy liczba usera jest złożona
# n = int(input("2. Podaj liczbe: "))
n = 420
boolCzyZlozona = False
for i in range(2,n):
    if n % i == 0:
         boolCzyZlozona = True
print(boolCzyZlozona)

#* 3. Czy liczba usera jest względnie pierwsza do 24
# n = int(input("3. Podaj liczbe: "))
n = 420
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a
if 1 == nwd(n,24):
    print(True)
else:
    print(False)

#* 4. Zaszyfruj s kluczem k w szyfrze cezara
def cesar(napis,k):
    szyfr = ""
    for i in range(len(napis)):
        szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + k) % 26)
    return szyfr
# s = input("4. s: ")
# k = input("4. k: ")
s = "KochamInformatyke"
k = 3
print(cesar(s,k))

#* 5. Dodaj dwa ułamki a/b + c/d
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
# a = input("5. a: ")
# b = input("5. b: ")
# c = input("5. c: ")
# d = input("5. d: ")
a,b,c,d=1,1,4,4
print(ulamkiSkracanie(ulamkiDodawanie(a,b,c,d,True)))
print(ulamkiMieszane(ulamkiDodawanie(a,b,c,d,False)))

#* 6. Znajdź NWW od usera
# a = input("6. a: ")
# b = input("6. b: ")
a,b=6,9
print(nww(a,b))

#! Napisy

#* 1. Znajdź ilość litrer C we wpisanym napisie
# napis = input("1. Podaj napis: ")
napis = "CECYLIA"
ilosc = 0
for i in range(len(napis)):
    if napis[i] == "C":
        ilosc += 1
print(ilosc)

#* 2. Sprawdź czy literki są w ciągu nierosnącym np. ZOO
# wejscie = input("1. Podaj napis: ")
wejscie = "ZOO"
def ciagMalejaccy(wejscie):
    alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]
    flaga = True
    for i in range(len(wejscie)-1):
        if alfabet.index(wejscie[i]) < alfabet.index(wejscie[i+1]):
            flaga = False
    return flaga
print(ciagMalejaccy(wejscie))

#* 3. Najdłuższy wyraz
napis1= "LOLEK"
napis2= "BOLEK"
napis3= "TROLEK"
# napis1,napis2,napis3 = input("3. 1: "),input("3. 2: "),input("3. 3: ")
if napis1 > napis2 and napis1 > napis3: print("1")
if napis2 > napis1 and napis2 > napis3: print("2")
if napis3 > napis2 and napis3 > napis1: print("3")