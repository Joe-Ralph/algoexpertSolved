def findFirstTwoNumberSum(arr,k):
    hashmap = dict()
    for i in arr:
        required = k-i
        if required in hashmap.keys():
            return (required,i)
        else:
            hashmap[i] = True
        
ans = findFirstTwoNumberSum([3,5,-4,8,11,1,-1,6],10)
print(ans)