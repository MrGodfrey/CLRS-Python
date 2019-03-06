# define a new class based on List
class myHeap(list):
    heapSize=0

    def maxHeapify(self,i):
        '''Assuming left(i) and right(i) is already maximum heap node, but i maybe not,
         recover the maximum property.'''

        large=i
        left=self.left(i)
        right=self.right(i)

        if left < self.heapSize:
            if self[left] < self[i]:
                large=i
            else:
                large=left
        if right < self.heapSize and self[large]<self[right]:
            large=right

        if large!=i:
            self[i],self[large]=self[large],self[i]
            self.maxHeapify(large)


    
    def __init__(self,list):
        "Build a max-heap by a unorder list."

        self.heapSize=len(list)
        for i in list:
            self.append(i)

        for i in reversed(range((self.heapSize>>1)+1)):
            self.maxHeapify(i)

    def heapMax(self):
        "Return max value in heap."
        return self[0]
    
    def heapExactMax(self):
        "Return tha maximum element in self, and delete it."
        if self.heapSize < 1:
            EnvironmentError("heap underflow")

        max=self[0]
        self[0]=self[self.heapSize-1]
        self.heapSize=self.heapSize-1
        self.maxHeapify(0)

        return max

    def heapIncreaseKey(self,i,key):
        "Assuming self[i]<key, and increase self[i] to key, contain maxmum property."
        self[i]=key
        parent=self.parent(i)
        while i and self[parent] < self[i]:
            self[parent],self[i]=self[i],self[parent]
            i=parent
            parent=self.parent(i)
        
        return self
    
    def maxHeapInsert(self,key):
        "Insert key to heap."
        self.append(-float("inf"))
        self.heapSize=self.heapSize+1
        self.heapIncreaseKey(self.heapSize-1,key)
        return self        

    def parent(self,i):
        "Return parent index of i"
        return int((i+1)/2)-1
    
    def left(self,i):
        "Return left child index of i"
        return 2*i+1
    
    def right(self,i):
        "Return right child index of i"
        return 2*i +2
    
def heapSort(A):
    "Sort list A by heapsort method."
    A=myHeap(A)

    while A.heapSize >1:
        A[A.heapSize-1],A[0]=A[0],A[A.heapSize-1]
        A.heapSize=A.heapSize-1
        A.maxHeapify(0)

    return A
    
    
a=myHeap([1,2,3,4,3,2,3,4,4,2])

print(a.maxHeapInsert(3)) 