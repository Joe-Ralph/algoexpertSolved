inp = [1,11,3,0,15,5,2,4,10,7,12,6]

def longestRange(arr):
    hashmap = {}
    bestRange = [None,None]
    maxRange = float('-inf')
    for i in arr:
        hashmap[i] = True
    for i in hashmap:
        if not hashmap[i]:
            continue
        currentRange = 0
        left = i-1
        right = i+1
        while left in hashmap:
            left-=1
            currentRange+=1
        while right in hashmap:
            right+=1
            currentRange+=1
        if currentRange > maxRange:
            maxRange = currentRange
            bestRange = [left+1,right-1]
    return bestRange
print(longestRange(inp))