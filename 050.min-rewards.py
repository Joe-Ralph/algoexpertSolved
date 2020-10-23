inp = [8,4,2,1,3,6,7,9,5]

def minRewards(arr):
    reverse = 0
    rewards = 0
    current = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            if reverse > 0:
                current = 0
                while reverse > 0:
                    current+=1
                    rewards+=current
                    reverse-=1
            current += 1
        else:
            reverse += 1

        rewards+=current
    return rewards

print(minRewards(inp))