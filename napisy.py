
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
