inp1 = 10
inp2 = [1,5,10,25]

# def noOfWays(amount,denominations):
#     dp = [0]*(amount+1)
#     dp[0] = 1
#     for i in range(len(denominations)):
#         for j in range(1,len(dp)):
#             if j >= denominations[i]:
#                 dp[j]+=dp[j-denominations[i]]
#     return dp[-1]

def noOfWays(amount,denominations, cnt):
    if amount == 0: 
        return cnt+1
    for ind, d in enumerate(denominations):
        if amount-d >=0:
            cnt = noOfWays(amount-d,denominations[ind:], cnt)
    return cnt

print(noOfWays(inp1, inp2,0))