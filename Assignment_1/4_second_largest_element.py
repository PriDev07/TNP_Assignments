
# 4. Find the Second Largest Element

import sys
def secondLargest(arr):
    largest=-sys.maxsize-1
    ans = -sys.maxsize-1
    size = len(arr)
    for i in range(size):
        if arr[i]>largest:
            largest = arr[i]
    for i in range(size):
        if arr[i]==largest:
            continue
        if arr[i]>ans:
            ans = arr[i]
    return ans




arr = [110,2,5,-50,4,8,150]
ans = secondLargest(arr)
print("Second Largest element is :",ans)