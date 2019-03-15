import random

def partition(A,p,r):
    x=A[r-1]
    i=p-1
    for j in range(p,r):
        if A[j] < x:
            i=i+1
            A[i], A[j]=A[j],A[i]
    A[i+1],A[r-1]=A[r-1],A[i+1]
    return i+1

def randomPartition(A,p,r):
    i=random.randint(p,r-1)
    A[r-1],A[i]=A[i],A[r-1]
    return partition(A,p,r)

def quickSort(A,p,r):
    if p<r-1:
        q=randomPartition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)
    return


# Test part
if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3,1,2,3,3,3]
    quickSort(A,0,len(A))
    print(A)