
#* Sortowanie stringa - String -> Lista -> String
def sortowanieStringa(s):
    L = list(s)
    L.sort()
    w = "".join(L)
    return w
#* Palindrom
def czyPalindrom(s):
    L,R = list(s),list(s)
    R.reverse()
    if L == R:
        return True
    else:
        return False
#* Anagram
def czyAnagram(a,b):
    X, Y = list(a), list(b)
    X.sort()
    Y.sort()
    a, b = "".join(X), "".join(Y)
    if a == b:
        return True
    else:
        return False

#* Ciąg Malejący
def ciagMalejacy(wejscie):
    alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]
    flaga = True
    for i in range(len(wejscie)-1):
        if alfabet.index(wejscie[i]) < alfabet.index(wejscie[i+1]):
            flaga = False
    return flaga