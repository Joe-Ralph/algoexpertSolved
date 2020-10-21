inp = [7,10,12,7,9,14]

def maxSubsetSum(arr):
    res = arr[:]
    for i in range(len(res)):
        if i == 0: res[i]=arr[i]
        elif i == 1: res[i]=max(arr[0],arr[1])
        else: res[i]=max(res[i-1],res[i-2]+arr[i])
    return res[-1]

print(maxSubsetSum(inp))