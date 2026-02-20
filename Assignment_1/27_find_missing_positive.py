# 27. Find the First Missing Positive
# Find smallest positive integer missing from array

def firstMissingPositive(arr):
    st = set(arr)
    i = 1

    while True:
        if i not in st:
            return i
        i += 1


arr = [3, 4, -1, 1]
ans = firstMissingPositive(arr)
print(ans)
