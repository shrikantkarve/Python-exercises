A = [10,80,90,40,50,20,50]
#A = [10,80,90,40,50,20,50]

def qsort(A,lo,hi):
    if lo < hi:
        p = partition(A,lo,hi)
        qsort(A,lo, p-1)
        qsort(A, p+1, hi)

def partition(A, lo, hi):
    print(A)
    p = A[hi]
    i = lo
    for j in range(lo, hi+1):
       if A[j] < p:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[hi] = A[hi],A[i]
    return i

qsort(A,0,len(A)-1)
print(A)
