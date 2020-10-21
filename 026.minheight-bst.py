class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def minHeight(root):
    if root is None:
        return -1
    return min(minHeight(root.left), minHeight(root.right))+1



tree = Tnode(5)
tree.left = Tnode(2)
tree.right = Tnode(9)
tree.left.left = Tnode(1)
tree.left.right = Tnode(3)
tree.right.left = Tnode(7)
tree.right.right = Tnode(12)

print(minHeight(tree))
