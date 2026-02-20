# 24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

def rearrangeAlternatively(arr):
    arr.sort()
    size = len(arr)
    i = 0
    j = size-1
    ans=[]
    while(i<j):
        ans.append(arr[i])
        ans.append(arr[j])
        i+=1
        j-=1
    return ans

arr = [1,2,3,4,5,6]
ans = rearrangeAlternatively(arr)
print(ans)