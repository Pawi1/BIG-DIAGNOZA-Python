
#* Sortowanie quicksort Hoare
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
#* Sortowanie quicksort Lomuto
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

#* Sortowanie poprzez wstawianie
def insertionSort(A):
     
    if (n := len(A)) <= 1:
      return
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
#* Sortowanie bąbelkowe
def bubbleSort(T):
    n = len(T)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if T[i] > T[i+1]:
                T[i], T[i+1] = T[i+1], T[i]
#* Sortowanie poprzez wybieranie
def selectionSort(T):
    n = len(T)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if T[j] < T[k]:
                k = j
        T[k], T[i] = T[i], T[k]

