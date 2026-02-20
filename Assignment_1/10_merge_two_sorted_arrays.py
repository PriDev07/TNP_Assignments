# 10. Merge Two Sorted Arrays
# Merge two already sorted arrays into one sorted array

def mergeSortedArrays(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # Remaining elements
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
ans = mergeSortedArrays(arr1, arr2)
print(ans)