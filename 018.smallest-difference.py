inp1 = [-1,5,10,20,28,3]
inp2 = [26,134,135,15,17]

def smallestDifference(arr1, arr2):
    ans = [None,None]
    minDiff = float('inf')
    l = r = 0
    arr1.sort()
    arr2.sort()
    while l < len(arr1) and r < len(arr2):
        currDiff = abs(arr1[l] - arr2[r])
        if currDiff < minDiff:
            minDiff = currDiff
            ans[0]=l;ans[1]=r
        if arr1[l] > arr2[r]:
            r+=1
        else:
            l+=1
    return [arr1[ans[0]], arr2[ans[1]]]

print(smallestDifference(inp1, inp2))