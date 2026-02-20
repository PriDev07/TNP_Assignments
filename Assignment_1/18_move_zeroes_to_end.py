# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def moveZeroes(arr):
    last_non_zero = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero], arr[i] = arr[i], arr[last_non_zero]
            last_non_zero += 1
    return arr

arr = [3,0,2,1,0,2,0,1]
ans = moveZeroes(arr)
print(ans)