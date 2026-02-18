import sys

# 2. Find the Maximum & Minimum Element

#Function for finding max and min value
def maxAndMin(arr):
    size = len(arr)
    min = sys.maxsize+1
    max = -sys.maxsize-1
    for i in range(size):
        if arr[i]<min:
           min = arr[i]
        if arr[i]>max:
           max = arr[i]
    return max,min



arr = [110,2,5,-50,4,8]
max,min = maxAndMin(arr)
print("max value", max)
print("min value",min)