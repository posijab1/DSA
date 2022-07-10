def MaximumSubarray(array):
    maxSubArray = array[0]
    curSum = 0

    for n in array:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSubArray = max(maxSubArray, curSum)
    return maxSubArray

print(MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))



