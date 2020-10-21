inp = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]

def longestPeak(arr):
    all_peaks_index = []
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            all_peaks_index.append(i)
    longestPeaklen = 0
    for i in all_peaks_index:
        leftidx = i-1
        while leftidx >= 0 and arr[leftidx] < arr[leftidx+1]:
            leftidx -= 1
        rightidx = i+1 
        while rightidx < len(arr) and arr[rightidx] < arr[rightidx-1]:
            rightidx += 1
        currpeaklen = rightidx - leftidx -1 
        if currpeaklen > longestPeaklen:
            longestPeaklen = currpeaklen
    return longestPeaklen

print(longestPeak(inp))