
# 32. Find Maximum Product Pair
# Find two elements whose product is maximum

def maxProductPair(arr):
    size = len(arr)
    if size < 2:
        return None

    arr.sort()

    product1 = arr[size - 1] * arr[size - 2]
    product2 = arr[0] * arr[1]

    if product1 > product2:
        return (arr[size - 2], arr[size - 1])
    else:
        return (arr[0], arr[1])


arr = [-10, -3, 5, 6, -2]
ans = maxProductPair(arr)
print(ans)
