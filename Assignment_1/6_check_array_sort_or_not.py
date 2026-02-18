# 6. Check if Array is Sorted
def checkSortedArray(arr):
    size = len(arr)
    for i in range(size-1):
        if arr[i]>arr[i+1]:
            return False
    
    return True

arr = [1,2,70,4,5,6,78]
ans = checkSortedArray(arr)
if ans:
    print("Sorted")
else:
    print("Not Sorted")