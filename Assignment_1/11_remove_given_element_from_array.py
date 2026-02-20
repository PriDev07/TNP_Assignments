# 11. Remove given Element from Array

def remGivenEle(arr,ele):
    size = len(arr)
    newArr = [x for x in arr if x != ele]
    return newArr

arr = [1,1,1,2,4,5,3,24]
x = remGivenEle(arr,5)
print(x)