# 15. Find Union of Two Arrays

def findUnion(arr1,arr2):
    ans = set()
    size1 = len(arr1)
    size2 = len(arr2)
    for i in range(size1):
        if arr1[i] not in ans:
            ans.add(arr1[i])
    for i in range(size2):
        if arr2[i] not in ans:
            ans.add(arr2[i])
    return ans


arr1 = [1,1,1,2,4,5,3,24]
arr2 = [1,1,1,2,3]

ans = findUnion(arr1,arr2)
print(ans)