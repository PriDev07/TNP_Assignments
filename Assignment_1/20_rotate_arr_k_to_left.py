# 20. Rotate Array to the Left by k Positions

def rev(arr,a,b):
    size = len(arr)
    # a=0
    # b=size-1
    while a<b:
        arr[a],arr[b] = arr[b],arr[a]
        a+=1
        b-=1
    return arr

def rotByK(arr,k):
    size = len(arr)
    ans = rev(arr,0,size-1)
    ans = rev(arr,0,size-k-1)
    ans = rev(arr,size-k,size-1)
    return ans


arr = [1,2,3,4,5,6]
ans = rotByK(arr,6)
print(ans)