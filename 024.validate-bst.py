class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isBST(root):
    return isBSTUtil(root,float('-inf'),float('+inf'))

def isBSTUtil(root,mi,ma):
    if root is None:
        return True
    if not mi < root.val < ma:
        return False
    return isBSTUtil(root.left,mi,root.val) and isBSTUtil(root.right,root.val,ma)

tree = Tnode(5)
tree.left = Tnode(2)
tree.right = Tnode(9)
tree.left.left = Tnode(1)
tree.left.right = Tnode(3)
tree.right.left = Tnode(7)
tree.right.right = Tnode(12)

print(isBST(tree))
