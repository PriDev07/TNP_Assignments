# 25. Find Majority Element: Find the element that appears more than n/2 times.

# Moore's Voting Algo




def majorityElement(arr):
    count =0
    size = len(arr)
    candidate=-1
    # Find eligible candidate 
    for i in range(size):
        if count==0:
            candidate = arr[i]
            count=1
        if candidate == arr[i]:
            count+=1
        else:
            count -=1
    
    # Now verify Candidate > n/2
    verify =0
    for i in range(size):
        if arr[i]==candidate:
            verify+=1
    if verify>size/2:
        return candidate
    else:
        return -1

arr = [1,1,1,2,2,2,2,2,2,3,5]
ans = majorityElement(arr)
print(ans)