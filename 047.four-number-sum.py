inp1 = [7,6,4,-1,1,2]
inp2 = 16

# def fourNumberSum(arr,val):
#     x = len(arr)
#     ans = set()
#     for i in range(x):
#         for j in range(x):
#             if i==j: continue
#             for k in range(x):
#                 if k==i or k==j:
#                     continue
#                 for l in range(x):
#                     if l==i or l==j or l==k:
#                         continue
#                     if arr[i]+arr[j]+arr[k]+arr[l] == val:
#                         ans.add(tuple(sorted([arr[i],arr[j],arr[k],arr[l]])))
#     return [list(i) for i in list(ans)]



def fourNumberSum(arr, val):
    hashmap = {}
    quadruplets = []
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):
            pairSum = arr[i] + arr[j]
            if val - pairSum in hashmap:
                for pair in hashmap[val - pairSum]:
                    quadruplets.append(pair+[arr[i],arr[j]])
        for k in range(i):
            pairSum = arr[i] + arr[k]
            if pairSum in hashmap:
                hashmap[pairSum].append([arr[i],arr[k]])
            else:
                hashmap[pairSum] = [[arr[i],arr[k]]]
    return quadruplets

print(fourNumberSum(inp1,inp2))