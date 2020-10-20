arr = [1,5,10,1100,1100,1101,1102,9001]

def isMonotonic(arr):
    decreasing = True
    increasing = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            increasing = False
        if arr[i] < arr[i+1]:
            decreasing = False
    return increasing or decreasing

print(isMonotonic(arr))