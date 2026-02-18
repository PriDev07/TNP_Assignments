# 1. Reverse an Array
# Reverse function
def rev(arr):
    size = len(arr)
    a=0
    b=size-1
    while a<b:
        arr[a],arr[b] = arr[b],arr[a]
        a+=1
        b-=1
    return arr


arr = [110,2,5,1,4,8]
ans = rev(arr)
print(ans)