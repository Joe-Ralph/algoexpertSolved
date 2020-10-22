inp = [[1,2,3],[4,5,6],[7,8,9]]

def searchInSortedMatrix(matrix, searchValue):
    col = 0;row = len(matrix[-1])-1
    while(row>=0 and col<len(matrix)):
        if matrix[row][col] < searchValue:
            col+=1
        elif matrix[row][col] > searchValue:
            row-=1
        else:
            return (row,col)
    return (-1,-1)

print(searchInSortedMatrix(inp,4))