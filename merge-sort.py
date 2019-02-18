def merge(array,p,q,r):
    "Merge function. Sort the elements of the array[p...r-1] by merge two sorted subarraies,  array[p...q-1] and array[q...r-1]"

    # infinite in python is float('inf')

    L=array[p:q]
    R=array[q:r]
    L=L+[float('inf')]
    R=R+[float('inf')]
    i=0
    j=0
    for k in range(p,r):
        if L[i] <= R[j]:
            array[k]=L[i]
            i=i+1
        else:
            array[k]=R[j]
            j=j+1

    return array

def mergeSort(array,p,r):
    "Merge sort. Sort the elements of the array[p..r]"

    # reset the terminate condiction of recursion
    if p < r-1:
        q=int((p+r)/2)
        mergeSort(array,p,q)
        mergeSort(array,q,r)
        merge(array,p,q,r)
    return array

# Test part
if __name__ == "__main__":
    A = [0,3,5,1,2,4,6,9,8,11,22,13]
    mergeSort(A,0,len(A))
    print(A)
