inp = [1,2,4,7,10,11,7,12,6,7,16,18,19]

def findMinSubarrayToSort(arr):
    ans = [0,len(arr)-1]
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            ans[0] = i+1
        else:
            break
    for j in range(len(arr)-1,1,-1):
        if arr[j] >= arr[j-1]:
            ans[1] = j-1
        else:
            break
    minVal,maxVal = min(arr[ans[0]:ans[1]]),max(arr[ans[0]:ans[1]])
    for i in range(len(arr)):
        if minVal < arr[i]:
            ans[0] = i-1
            break
    for i in range(len(arr)-1,0,-1):
        if maxVal > arr[i]:
            ans[1] = i
            break
    return ans
print(findMinSubarrayToSort(inp))