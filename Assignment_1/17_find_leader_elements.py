# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def leaderElements(arr):
    ans = [arr[-1]]
    size = len(arr)
    currMax = -1
    for i in range(size-2,-1,-1):
        if arr[i]>currMax:
            currMax = arr[i]
            ans.append(arr[i])
    return ans

arr = [ 10,12,8,6,10,2,4,1]
ans = leaderElements(arr)
print(ans)