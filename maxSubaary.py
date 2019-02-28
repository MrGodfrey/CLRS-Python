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
    
    return [leftLow,rightHigh+1,lmaxSum+rmaxSum]

def maxSubarray(low,high)->[int,int,int]:
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
            

# Test part
if __name__ == "__main__":
    A=[-1,2,18,-2,-4,55,-6]
    left,right,maxSum=maxSubarray(0,len(A))
    print(f'The array is {A}')
    B=A[left:right]
    print(f'The max sum subarray is {B}, and the max sum is {maxSum}.')
