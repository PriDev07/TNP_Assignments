# 28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.

# Using 3 pointers:

def sortThreeElements(arr):
    size = len(arr)
    zeroes =0
    ones =0
    twos=0
    for i in range(size):
        if arr[i]==0:
            zeroes+=1
        elif arr[i]==1:
            ones+=1
        else:
            twos+=1
    ans =[]
    while(zeroes>0):
        ans.append(0)
        zeroes-=1
    while(ones>0):
        ans.append(1)
        ones-=1
    while(twos>0):
        ans.append(2)
        twos-=1
    return ans

arr = [0,1,0,1,1,2,0]
ans = sortThreeElements(arr)
print(ans)
