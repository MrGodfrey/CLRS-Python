def crossMaxSubarray(low,high,middle)->[int,int,int]:
    lmaxSum=-float('inf')
    totalSum=0
    for lIndex in range(middle-1,low-1,-1):
        totalSum=totalSum+A[lIndex]
        if totalSum >lmaxSum:
            leftLow=lIndex
            lmaxSum=totalSum
    
    rmaxSum=-float('inf')
    totalSum=0
    for rIndex in range(middle,high,1):
        totalSum=totalSum+A[rIndex]
        if totalSum >rmaxSum:
            rightHigh=rIndex
            rmaxSum=totalSum
    
    # +1 because the index rIndex point to subarray's last elements, but rightHigh should 
    # point to the elements after that.
    return [leftLow,rightHigh+1,lmaxSum+rmaxSum]

def maxSubarray(low,high)->[int,int,int]:
    "Find A[low:high-1]'s sub-array which has the largest summation among other subarrays."
    if low >= high-1:
        return [low,high,A[low]]
    else:
        middle=int((high+low)/2)
        [leftLow,leftHigh,leftSum]=maxSubarray(low,middle)
        [rightLow,rightHigh,rightSum]=maxSubarray(middle,high)
        [crossLow,crossHigh,crossSum]=crossMaxSubarray(low,high,middle)
        if leftSum >= rightSum and leftSum >= crossSum:
            return [leftLow,leftHigh,leftSum]
        elif crossSum >= rightSum and crossSum >= leftSum:
            return [crossLow,crossHigh,crossSum]
        else:
            return [rightLow,rightHigh,rightSum]
            
def linearMaxSubarray(array):
    "Exercise 4.1.5, linear-time algorithm for the maximum-subarray problem"
    n=len(array)
    r=l=0
    maxSum=array[l]
    rightSum=0

    # search for the right index of maximum-subarray
    for j in range(1,n):
        rightSum=rightSum+array[j]
        if rightSum  >= 0:
            r=j
            maxSum=maxSum+rightSum
            rightSum=0

    # search for the left index of maximum-subarray
    l=r
    leftSum=0
    for j in reversed(range(r)):
        leftSum=leftSum+array[j]
        if leftSum >0:
            l=j
            leftSum=0

    maxSum=maxSum-leftSum
    
    return [l,r+1,maxSum]

# Test part
if __name__ == "__main__":
    A=[1,2,-10,3,4,5,-6,8,10,2,4,6,-17,5]
    left,right,maxSum=maxSubarray(0,len(A))
    print(f'The array is {A}')
    B=A[left:right]
    print(f'The max sum subarray is {B}, and the max sum is {maxSum}.')

    left,right,maxSum=linearMaxSubarray(A)
    B=A[left:right]
    print(f'Use linear max subarray procedure.\nThe max sum subarray is {B}, and the max sum is {maxSum}.')
