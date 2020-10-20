def insertionSort(arr):
    for i in range(len(arr)):
        j=i
        while j-1 >= 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr

inp = [8,5,2,9,5,6,3]
print(insertionSort(inp))