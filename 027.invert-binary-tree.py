class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def invert(root):
    if root is None:
        return
    invert(root.left)
    invert(root.right)
    root.left,root.right = root.right,root.left

def inorder(root,res):
    if root is None:
        return
    inorder(root.left,res)
    res.append(root.val)
    inorder(root.right,res)
    return res

tree = Tnode(5)
tree.left = Tnode(2)
tree.right = Tnode(9)
tree.left.left = Tnode(1)
tree.left.right = Tnode(3)
tree.right.left = Tnode(7)
tree.right.right = Tnode(12)

print(inorder(tree,[]))
print(invert(tree))
print(inorder(tree,[]))
