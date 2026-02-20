# 23. Maximum Sum Subarray (Kadane's Algorithm)
# Find maximum possible sum of contiguous subarray

def maxSubArray(arr):
    maxCurrent = arr[0]
    maxGlobal = arr[0]

    for i in range(1, len(arr)):
        maxCurrent = max(arr[i], maxCurrent + arr[i])
        maxGlobal = max(maxGlobal, maxCurrent)

    return maxGlobal


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = maxSubArray(arr)
print(ans)
