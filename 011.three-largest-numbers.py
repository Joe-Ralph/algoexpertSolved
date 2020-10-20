inp = [141,1,17,-7,-17,-27,18,541,8,7,7]

def shiftArray(arr,idx):
    for i in range(idx):
        arr[i] = arr[i+1]
    return arr

def largestThreeNumbers(arr):
    ans = [None]*3
    for i in range(len(arr)):
        if ans[2] is None or arr[i] > ans[2]:
            ans = shiftArray(ans,2)
            ans[2] = arr[i]
        elif ans[1] is None or arr[i] > ans[1]:
            ans = shiftArray(ans,1)
            ans[1] = arr[i]
        elif ans[0] is None or arr[i] > ans[0]:
            ans = shiftArray(ans,0)
            ans[0] = arr[i]
    return ans

# print(largestThreeNumbers(inp))

def largestNNumbers(arr,n):
    ans = [None]*n
    for i in range(len(arr)):
        for j in range(n-1,-1,-1):
            if ans[j] is None or arr[i] > ans[j]:
                ans = shiftArray(ans,j)
                ans[j] = arr[i]
                break
    return ans

print(largestNNumbers(inp,5))