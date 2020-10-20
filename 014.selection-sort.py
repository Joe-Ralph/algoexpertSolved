def selectionSort(arr):
    for i in range(0, len(arr)):
        minIdx = i
        for j in range(i,len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[minIdx],arr[i] = arr[i],arr[minIdx]
    return arr
inp = [8,5,2,9,5,6,3]
print(selectionSort(inp))