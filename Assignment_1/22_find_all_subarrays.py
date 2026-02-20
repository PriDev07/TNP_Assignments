# 22. Find All Subarrays

def findSubArrays(arr):
    ans = [[]]
    size = len(arr)
    for i in range(size):
        newArr =[]
        for j in range(i,size):
            newArr.append(arr[j])
        ans.append(newArr)
    return ans

arr = [1,2,3,4,5,6]
ans = findSubArrays(arr)
print(ans)