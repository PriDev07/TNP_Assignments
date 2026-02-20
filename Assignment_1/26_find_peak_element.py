# 26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.

def findPeakElement(arr):
    size = len(arr)
    x=0
    j=2
    for i in range(1,size-1):
        if(arr[i]> arr[x] and arr[i]>arr[j]):
            return arr[i]
        x+=1
        j+=1
    return -1

arr = [2,1,3,1,4,5,6]
ans = findPeakElement(arr)
print(ans)