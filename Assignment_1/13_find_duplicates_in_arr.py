# 13. Find Duplicates in an Array

def findDup(arr):
    size = len(arr)
    dup = set()
    newList = set()
    for i in range(size):
        if arr[i] in dup:
            newList.add(arr[i])
        else:
            dup.add(arr[i])
    return newList

arr = [2,1,3,5,2]
dupArr = findDup(arr)
print(dupArr)