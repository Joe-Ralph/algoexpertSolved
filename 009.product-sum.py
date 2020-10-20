inp = [5,2,[7,-1],3,[6,[-13,8],4]]

def productSum(arr,depth = 1):
    su = 0
    for i in arr:
        if isinstance(i,list):
            su+=productSum(i,depth+1)
        else:
            su+=i
    return depth*su

print(productSum(inp))