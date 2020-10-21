inp1 = 11
inp2 = [1,5,6,9]

# def minNoOfCoins(amount,denominations):
#     dp = [float('inf')]*(amount+1)
#     dp[0]=0
#     for i in range(len(denominations)):
#         for j in range(1,amount+1):
#             if denominations[i]<=j:
#                 dp[j] = min(dp[j],dp[j-denominations[i]]+1)

#     return dp[-1]

def minNoOfCoins(amount,denominations, cnt):
    if amount == 0: 
        return cnt
    ret = float('inf')
    for d in denominations:
        if amount-d >=0:
            ret = min(ret,minNoOfCoins(amount-d,denominations, cnt+1))
    return ret

print(minNoOfCoins(inp1, inp2,0))