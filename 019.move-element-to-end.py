inp = [2,1,2,2,2,3,4,2]

def moveToEnd(arr,val):
    i=0
    j=len(arr)-1
    while(i<=j):
        if arr[i] == val and arr[j] != val:
            arr[i],arr[j] = arr[j],arr[i]
            j-=1;i+=1
        elif arr[i] != val:
            i+=1
        elif arr[j] == val:
            j-=1

    return arr 

print(moveToEnd(inp,2))