###################### pre
def nwd(a,b):
    while b > 0 :
        a, b = b, a % b
    return a
def nww(a,b):
    return (a*b//nwd(a,b))
##########################

def ulamkiDodawanie(a,b,c,d):
    print(f"{a}/{b} + {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} + {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)+(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)+(nww(b,d)//d*c))+"/"+ str((nww(b,d)))

def ulamkiUdejmowanie(a,b,c,d):
    print(f"{a}/{b} - {c}/{d} = {nww(b,d)//b*a}/{nww(b,d)} - {nww(b,d)//d*c}/{nww(b,d)} = {(nww(b,d)//b*a)-(nww(b,d)//d*c)}/{nww(b,d)} ")
    return str((nww(b,d)//b*a)-(nww(b,d)//d*c))+"/"+ str((nww(b,d)))

def ulamkiSkracanie(a_przez_b):
    a = int(a_przez_b[0])
    b = int(a_przez_b[2])
    return str(a//nwd(a,b))+"/"+str(b//nwd(a,b))

def ulamkiMieszane(a_przez_b):
    a = int(a_przez_b[0])
    b = int(a_przez_b[2])
    if a%b != 0:
        return str(a//b) +" "+ str(a%b)+"/"+str(b) 
    else: 
        return str(a)+"/"+str(b)
    