# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

def findMissingNo(arr):
    cnt = 1
    size = len(arr)
    arr.sort()
    for i in range(size):
        if arr[i]!=cnt:
            return cnt
        cnt+=1
    return "Nothing Missing"


arr = [2,1,3,5]
x =findMissingNo(arr)
print(x)