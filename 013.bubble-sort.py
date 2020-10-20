def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr
inp = [8,5,2,9,5,6,3]
print(bubbleSort(inp))