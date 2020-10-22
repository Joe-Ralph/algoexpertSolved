inp = 'abaxyzzyxf'

def longestPalindromicSubstring(string):
    lps = [0,1]

    for i in range(1, len(string)):
        odd = getlongestpalindromicFor(string,i-1,i+1)
        even = getlongestpalindromicFor(string,i-1,i)
        longest = max(odd,even,key = lambda x:x[1]-x[0])
        lps = max(lps,longest,key = lambda x:x[1]-x[0])
    return string[lps[0]:lps[1]]

def getlongestpalindromicFor(string,i,j):
    while i>=0 and j<len(string):
        if string[i]!=string[j]:
            break
        i-=1;j+=1
    return [i+1,j]


print(longestPalindromicSubstring(inp))
