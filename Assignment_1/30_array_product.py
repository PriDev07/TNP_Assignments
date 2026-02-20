# 30. Product of Array Except Self
# Given an array, return a new array where each element is the product of all elements except itself.
# Do not use division.

# Input: [1,2,3,4]
# Output: [24,12,8,6]

def productExceptSelf(arr):
    size = len(arr)
    prefix = [1] * size
    suffix = [1] * size
    ans = [1] * size

    for i in range(1, size):
        prefix[i] = prefix[i - 1] * arr[i - 1]

    for i in range(size - 2, -1, -1):
        suffix[i] = suffix[i + 1] * arr[i + 1]

    for i in range(size):
        ans[i] = prefix[i] * suffix[i]

    return ans


arr = [1, 2, 3, 4]
ans = productExceptSelf(arr)
print(ans)