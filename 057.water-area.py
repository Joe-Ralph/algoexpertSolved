inp = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]


def totalWaterCaptured(arr):
    leftMax = [0 for _ in range(len(arr))]
    rightMax = [0 for _ in range(len(arr))]
    leftMax[0] = arr[0]
    rightMax[len(arr)-1] = arr[len(arr)-1]
    for i in range(1,len(arr)):
        leftMax[i] = max(leftMax[i-1],arr[i-1])
    for i in range(len(arr)-2,-1,-1):
        rightMax[i] = max(rightMax[i+1],arr[i+1])
    waterCaptured = 0
    for i in range(len(arr)):
        waterCaptured+=min(leftMax[i],rightMax[i])-arr[i]
    print(leftMax,rightMax)
    return waterCaptured

print(totalWaterCaptured(inp))

# wait in here not yet