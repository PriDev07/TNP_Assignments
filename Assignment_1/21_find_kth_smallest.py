# Find the Kth Smallest Element

def findKSmallest(arr,ele):
    arr.sort()
    st = set()
    size = len(arr)
    for i in range(size):
        if arr[i] is not st:
            st.add(arr[i])
    newList = list(st)
    return newList[ele-1]

arr = [3,2,1,5,7,5,1,3,6,8]
ans = findKSmallest(arr,4)
print(ans)
