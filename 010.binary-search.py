def binarySearch(arr,value):
    l = 0
    r = len(arr)-1
    mid = (l+r)//2
    while l<=r:
        print(l,r,mid)
        if arr[mid] > value:
            r = mid-1
        elif arr[mid] < value:
            l = mid+1
        else:
            return mid
        mid = (l+r)//2
    return -1

inp = [0,1,21,33,45,45,61,71,72,73]

print(binarySearch(inp,73))
print(binarySearch(inp,33))
print(binarySearch(inp,0))