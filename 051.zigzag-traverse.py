inp =[[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]

def zigzag(arr):
    res = []
    isUp = False
    i=0;j=0
    m,n = len(arr),len(arr[0])
    while(i<m and j<n):
        res.append(arr[i][j])
        if isUp:
            i-=1;j+=1
        else:
            i+=1;j-=1
        if not (0<=i<m and 0<=j<n):
            if isUp:
                if j < n:
                    i+=1
                else:
                    j-=1;i+=2
            else:
                if i < m:
                    j+=1
                else:
                    i-=1;j+=2
            isUp = not isUp
    return res

print(zigzag(inp))