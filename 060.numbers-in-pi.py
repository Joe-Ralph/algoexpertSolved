inp1 = ['3141','5','31','2','4153','9','42']
inp2 = '3141532'

global minDepth
minDepth = float('inf')
def numbersInPi(arr,string):
    hashset  = set(arr)
    def numbersInPiUtil(string,start,depth):
        global minDepth
        print(string)
        if 0 == len(string):
            minDepth = min(depth-1,minDepth)
            return
        for i in range(1,len(string)+1):
            if string[:i] in hashset:
                numbersInPiUtil(string[i:],i+1,depth+1)
    numbersInPiUtil(string,1,0)
    return minDepth

print(numbersInPi(inp1,inp2))