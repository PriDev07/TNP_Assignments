# 31. Find Equilibrium Index
# Index where sum of left elements = sum of right elements

def findEquilibriumIndex(arr):
    totalSum = sum(arr)
    leftSum = 0

    for i in range(len(arr)):
        totalSum -= arr[i]
        if leftSum == totalSum:
            return i
        leftSum += arr[i]

    return -1


arr = [1, 3, 5, 2, 2]
ans = findEquilibriumIndex(arr)
print(ans)
