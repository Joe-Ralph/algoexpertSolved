inp1 = [10,15,8,12,94,81,5,2,11]
inp2 = [10,8,5,15,2,12,11,94,81]

def isBsts(arr1,arr2):
    if len(arr1) != len(arr2): return False
    if len(arr1)==0 and len(arr2)==0: return True
    if arr1[0] != arr2[0]: return False

    left1 = getSmaller(arr1)
    right1 = getGreater(arr1)
    left2 = getSmaller(arr2)
    right2 = getGreater(arr2)

    return isBsts(left1,left2) and isBsts(right1,right2)


def getSmaller(arr):
    small = []
    for i in range(1,len(arr)):
        if arr[i] < arr[0]: small.append(arr[i])
    return small

def getGreater(arr):
    greater = []
    for i in range(1,len(arr)):
        if arr[i] > arr[0]: greater.append(arr[i])
    return greater



print(isBsts(inp1,inp2))