inp = "ABC"

def permutations(string):
    x = []
    permuteUtil(list(string),0,len(string)-1,x)
    return x

def permuteUtil(string,l,r,ans):
    if l==r:
        ans.append(''.join(string))
    else:
        for i in range(l,r+1):
            string[i],string[l] = string[l],string[i]
            permuteUtil(string,l+1,r,ans)
            string[i],string[l] = string[l],string[i]

print(permutations(inp))