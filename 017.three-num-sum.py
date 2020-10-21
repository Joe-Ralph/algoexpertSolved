inp = [12,3,1,2,-6,5,-8,6]

def threeNumberSum(arr,val):
    ans = []
    arr.sort()
    for curr in range(len(arr)):
        l = curr + 1;r = len(arr)-1
        while(l<r):
            cs = arr[curr]+arr[l]+arr[r]
            if cs < val:
                l+=1
            elif cs > val:
                r-=1
            else:
                ans.append([arr[curr],arr[l],arr[r]])
                l+=1
                r-=1
    return ans

print(threeNumberSum(inp,0))