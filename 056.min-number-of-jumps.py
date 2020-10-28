# tempinp = [3,4,2,1,2,3]

inp = [3,4,2,1,2,3,7,1,1,1,3]



# minim = float('inf')
# O(product(arr)) , O(product(arr)) ! Dont Use
# def minJumpsRec(arr):
#     minJumpsUtil(arr,0,0)
#     return minim
# def minJumpsUtil(arr,jumps,idx):
#     global minim
#     if idx >= len(arr):
#         return
#     if idx == len(arr)-1:
#         if jumps < minim: minim = jumps
#         return
#     for i in range(1,arr[idx]+1):
#         minJumpsUtil(arr,jumps+1,idx+i)


# print(minJumpsRec(tempinp))

def minJumps(arr):
    jumps = [float('inf') for _ in range(len(arr))]
    jumps[0] = 0
    for i in range(1,len(arr)):
        for j in range(i):
            if j+arr[j] >= i:
                jumps[i] = min(jumps[i],jumps[j]+1)
    return jumps[-1]

print(minJumps(inp))