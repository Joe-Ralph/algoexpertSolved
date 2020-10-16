def isValidSubsequence(arr,sub):
    x = len(sub)
    ap = sp = 0
    while ap<len(arr):
        if sp == x: return True
        if arr[ap] == sub[sp]:
            sp+=1
        ap+=1
    return False

print(isValidSubsequence([5,1,22,25,6,-1,8,10,11,7],[1,6,-1,14]))