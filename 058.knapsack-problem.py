cost = [1,4,5,6]
weight = [2,3,6,7]

amount = 10

def knapsack(amount,cost,weight):
    dp = [[None for _ in range(amount+1)] for _ in range(len(weight)+1)]
    for i in range(amount+1):
        dp[0][i] = 0
    for i in range(1,len(cost)+1):
        for j in range(amount+1):
            if j>=weight[i-1]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]]+cost[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    indexOfChosenItems = getKnapsackItems(dp,weight)
    return (dp[-1][-1],indexOfChosenItems)

def getKnapsackItems(dp,weight):
    i = len(dp)-1
    j = len(dp[0])-1
    ans =[]
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append(i-1)
            j-=weight[i-1]
        i-=1
    return list(reversed(ans))
        

print(knapsack(amount,cost,weight))