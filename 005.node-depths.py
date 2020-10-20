class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def nodeDepths(root,sum):
    if not root:
        return 0
    def nodeDepthsUtil(root,depth):
        res=0
        if root.left:
            res+=nodeDepthsUtil(root.left,depth+1)
        if root.right:
            res+=nodeDepthsUtil(root.right,depth+1)
        return res+depth

    return nodeDepthsUtil(root,sum)

tree = Tnode(1)
tree.left = Tnode(2)
tree.right = Tnode(3)
tree.left.left = Tnode(4)
tree.left.right = Tnode(5)
tree.right.left = Tnode(6)
tree.right.right = Tnode(7)
tree.left.left.left = Tnode(8)
tree.left.left.right = Tnode(9)
tree.left.right.left = Tnode(10)
print(nodeDepths(tree,0))
