inp = [2,3,1,-4,-4,2]

def isSingleCycle(arr):
    count = 1
    i = arr[0]
    x = len(arr)
    while count <= x:
        i += arr[i]
        count+=1
        if i < 0: i+=x
        elif i >= x: i-=x
        elif i == 0:
            return True if count == x else False
    return False

print(isSingleCycle(inp))