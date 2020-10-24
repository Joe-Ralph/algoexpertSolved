inp1 = "xkykzpw"
inp2 = "zxvvyzw"


def longestCommonSubsequence(string1, string2):
    dp = [['' for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + string1[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    return dp[-1][-1]
print(longestCommonSubsequence(inp1, inp2))