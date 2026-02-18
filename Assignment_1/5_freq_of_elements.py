
def storeFreq(arr):
    output = {}
    size = len(arr)
    for i in range(size):
        if arr[i] in output:
            output[arr[i]]+=1
        else:
            output[arr[i]]=1
    return output

def getFreq(arr, ele):
    storedVal = storeFreq(arr)
    return storedVal.get(ele,0)

arr = [3,2,5,4,5,3,2,1]
print("Frequency of 2 in array is :", getFreq(arr,2))
