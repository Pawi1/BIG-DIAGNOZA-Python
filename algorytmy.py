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

##* Ułamki
#* Dodawanie
def ulamkiDodawanie(a,b,c,d):
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)/{nww(b,d)} }")
    return (nww(b,d)//b*a)+(nww(b,d)//d*c)/nww(b,d)
#* Odejmowanie
def ulamkiUdejmowanie(a,b,c,d):
    print(f"{a}/{b} - {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} - {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)-(nww(b,d)//d*c)/{nww(b,d)} }")
    return (nww(b,d)//b*a)+(nww(b,d)//d*c)/nww(b,d)

