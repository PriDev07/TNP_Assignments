# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.

def findIntersection(arr1,arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    st = set()
    ans = []
    for i in range(size2):
        st.add(arr1[i])
    for i in range(size1):
        if arr1[i] in st:
            ans.append(arr1[i])
    return ans


arr1 = [1,1,1,2,4,5,3,24]
arr2 = [1,1,1,2,3]
ans = findIntersection(arr1,arr2)
print(ans)