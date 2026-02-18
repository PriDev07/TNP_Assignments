
# 3. Find the Sum of Elements

# Function for sum of array
def sumOfArray(arr):
    size = len(arr)
    sum=0
    for i in range(size):
        sum+=arr[i]
    return sum


arr = [110,2,5,-50,4,8]
ans = sumOfArray(arr)
print("Sum of array is : ",ans)