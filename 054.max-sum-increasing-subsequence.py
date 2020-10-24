inp = [8,12,2,3,15,5,7]

def maxSumIncreasingSubsequence(arr):
    dp = arr[:]
    seq = [None for _ in arr]
    maxIndex = 0
    for i in range(len(dp)):
        for j in range(0,i):
            if arr[j] < arr[i] and dp[i] <= arr[i] + dp[j]:
                dp[i] = arr[i] + dp[j]
                seq[i] = j
        if dp[maxIndex] < dp[i]: maxIndex = i
    return obtainSequence(seq, maxIndex,arr)

def obtainSequence(seq, maxIndex,arr):
    result = []
    while maxIndex is not None:
        result.append(arr[maxIndex])
        maxIndex  = seq[maxIndex]

    return sorted(result)


print(maxSumIncreasingSubsequence(inp))