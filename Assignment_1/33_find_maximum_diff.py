# 33. Find Maximum Difference (j > i)
# Find maximum value of arr[j] - arr[i] such that j > i

def maxDifference(arr):
    if len(arr) < 2:
        return 0

    minElement = arr[0]
    maxDiff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        currentDiff = arr[i] - minElement
        if currentDiff > maxDiff:
            maxDiff = currentDiff

        if arr[i] < minElement:
            minElement = arr[i]

    return maxDiff


arr = [7, 1, 5, 3, 6, 4]
ans = maxDifference(arr)
print(ans)