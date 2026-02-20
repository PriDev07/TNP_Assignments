# 29. Find the Longest Consecutive Sequence
# Return length of longest consecutive elements sequence

def longestConsecutive(arr):
    st = set(arr)
    longest = 0

    for num in st:
        # Start only if it is beginning of sequence
        if num - 1 not in st:
            currentNum = num
            count = 1

            while currentNum + 1 in st:
                currentNum += 1
                count += 1

            longest = max(longest, count)

    return longest


arr = [100, 4, 200, 1, 3, 2]
ans = longestConsecutive(arr)
print(ans)