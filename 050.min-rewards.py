inp = [8,4,2,1,3,6,7,9,5]

def minRewards(arr):
    rewards = [1 for _ in range(len(arr))]
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            rewards[i+1] = rewards[i]+1
    for i in range(len(arr)-1,0,-1):
        if arr[i] < arr[i-1]:
            rewards[i-1] = max(rewards[i-1],rewards[i]+1)
    return sum(rewards)

print(minRewards(inp))