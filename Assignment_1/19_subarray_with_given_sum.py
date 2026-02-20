def subArrayWithSumK(arr, reqSum):
    left = 0
    currSum = 0
    
    for right in range(len(arr)):
        currSum += arr[right]
        
        while currSum > reqSum and left <= right:
            currSum -= arr[left]
            left += 1
        
        if currSum == reqSum:
            return left, right
    
    return -1, -1


arr = [1,4,20,3,10,5]
ans = subArrayWithSumK(arr,33)

if ans != (-1,-1):
    print(arr[ans[0]:ans[1]+1])
else:
    print("No subarray found")