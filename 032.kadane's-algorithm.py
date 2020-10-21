inp = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

def maxSubsetSum(arr):
    totalMax = float('-inf')
    currMaxsum = arr[0]
    for i in range(1,len(arr)):
        currMaxsum = max(arr[i],currMaxsum+arr[i])
        if totalMax < currMaxsum: totalMax = currMaxsum
    return totalMax

print(maxSubsetSum(inp))