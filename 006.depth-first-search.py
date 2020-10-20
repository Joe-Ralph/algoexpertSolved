graph  = dict()
graph['a'] = ['b','c','d']
graph['b'] = ['e','f']
graph['c'] = []
graph['d'] = ['g','h']
graph['e'] = []
graph['f'] = ['i','j']
graph['g'] = ['k']
graph['h'] = []
graph['i'] = []
graph['j'] = []
graph['k'] = []


def DFSIterative(graph,src):
    ans = []
    stack = []
    if graph is None:
        return ans
    stack.append(src)
    while stack:
        node = stack.pop()
        ans.append(node)
        for i in graph[node]:
            stack.append(i)
    return ans

def DFS(graph,src):
    def dfsUtil(graph,src,ans):
        ans.append(src)
        for i in graph[src]:
            dfsUtil(graph,i,ans)
        return ans
    return dfsUtil(graph,src,[])

print(DFSIterative(graph,'a'))
# print(DFS(graph,'a'))