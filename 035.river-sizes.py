inp = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]

def riverSizes(mat):
    visited = [[False for j in range(len(mat[i]))] for i in range(len(mat))]
    res = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if visited[i][j]:
                continue
            DFSOnRiver(i,j,mat,visited,res)
    return sorted(res)

def DFSOnRiver(i,j,mat,visited,res):
    riverSize = 0
    stack = [[i,j]]

    while stack:
        currentNode = stack.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if mat[i][j] == 0:
            continue
        riverSize += 1
        for i in getUnvisitedNeighbors(i,j,mat,visited):
            stack.append(i)
    if riverSize > 0:
        res.append(riverSize)

def getUnvisitedNeighbors(i,j,mat,visited):
    ans = []
    if 0 <= i-1 < len(mat) and 0<=j < len(mat[0]) and not visited[i-1][j]:
        ans.append([i-1,j])
    if 0 <= i < len(mat) and 0<=j-1 < len(mat[0]) and not visited[i][j-1]:
        ans.append([i,j-1])
    if 0 <= i+1 < len(mat) and 0<=j < len(mat[0]) and not visited[i+1][j]:
        ans.append([i+1,j])
    if 0 <= i < len(mat) and 0<=j+1 < len(mat[0]) and not visited[i][j+1]:
        ans.append([i,j+1])
    return ans
print(riverSizes(inp))