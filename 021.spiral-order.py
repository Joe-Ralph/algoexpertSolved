inp = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

def spiralOrder(arr):
    result = []
    sR,eR = 0,len(arr)-1
    sC,eC = 0,len(arr[0])-1

    while sR <= eR and sC <= eC:
        for i in range(sC,eC+1):
            result.append(arr[sR][i])

        for i in range(sR+1,eR+1):
            result.append(arr[i][eC])

        for i in range(eR-1,sC-1,-1):
            result.append(arr[eR][i])

        for i in range(eR-1,sR,-1):
            result.append(arr[i][sC])

        sR+=1;sC+=1;eR-=1;eC-=1
    return result

def spiralOrderRecursive(arr):
    res =[]
    spiralOrderUtil(arr,0,len(arr)-1,0,len(arr[0])-1,res)
    return res

def spiralOrderUtil(arr,sR,eR,sC,eC,result):
    if sR > eR or sC > eC :
        return

    for i in range(sC,eC+1):
        result.append(arr[sR][i])

    for i in range(sR+1,eR+1):
        result.append(arr[i][eC])

    for i in range(eR-1,sC-1,-1):
        result.append(arr[eR][i])

    for i in range(eR-1,sR,-1):
        result.append(arr[i][sC])

    spiralOrderUtil(arr,sR+1,eR-1,sC+1,eC-1,result)


print(spiralOrderRecursive(inp))