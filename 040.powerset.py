inp = [1,2,3]

def powerset(arr):
    subsets = [[]]
    for element in arr:
        for i in range(len(subsets)):
            print(i,subsets)
            current = subsets[i]
            subsets.append(current+[element])
    return subsets

def powersetAnother(arr):
    subsets=[[]]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            subsets.append(arr[i:j])
    return sorted(subsets,key=len)
print(powersetAnother(inp))