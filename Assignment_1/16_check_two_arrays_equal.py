# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements

def checkArrayEqual(arr1,arr2):
    arr1.sort()
    arr2.sort()
    if len(arr1) != len (arr2):
        return "Not Equal"
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return "Not Equal"
    return "Equal"

arr1 = [1,1,1,2,3]
arr2 = [1,1,1,2,3]
ans = checkArrayEqual(arr1,arr2)
print(ans)