# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

def pairSum(arr,sum):
    arr.sort()
    size = len(arr)
    a = 0
    b = size-1
    while(a<b):
        if(arr[a]+arr[b]==sum):
            return a,b
        elif(arr[a]+arr[b]>sum):
            b-=1
        else:
            a+=1
    return "No Pairs found"

arr = [1,2,3,4,5,6]
ans = pairSum(arr,12)
print(ans)