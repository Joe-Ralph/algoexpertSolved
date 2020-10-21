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


def BFSIterative(graph,src):
    ans = []
    queue = []
    if graph is None:
        return ans
    queue.append(src)
    while queue:
        node = queue.pop(0)
        ans.append(node)
        for i in graph[node]:
            queue.append(i)
    return ans


print(BFSIterative(graph,'a'))