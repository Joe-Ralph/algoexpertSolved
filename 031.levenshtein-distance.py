inp1 = 'abc'
inp2 = 'yabd'

def levenshteinDistance(str1, str2):
    m,n = len(str1)+1, len(str2)+1
    dp = [[None for i in range(n)]for i in range(m)]
    for i in range(n):
        dp[0][i] = i
    for i in range(m):
        dp[i][0] = i
    for i in range(1,m):
        for j in range(1,n):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
    return dp[-1][-1]


print(levenshteinDistance(inp1, inp2))