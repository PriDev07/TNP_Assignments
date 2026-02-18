# 9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

def removeDuplicates(arr):
    ans=[]
    seen = set()
    for num in arr:
        if num not in seen:
            seen.add(num)
            ans.append(num)
    return ans
arr = [1,1,1,2,4,5,3,24]
ans = removeDuplicates(arr)
print(ans)