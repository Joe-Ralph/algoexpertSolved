class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root,val1,val2):
    if root is None:
        return None
    if(root.val == val1 or root.val == val2):
        return root
    x = lowestCommonAncestor(root.left,val1,val2)
    y = lowestCommonAncestor(root.right,val1,val2)
    if x is not None and y is not None:
        return root
    elif x is not None or y is not None:
        return y if x is None else x
    else:
        return None

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
print(lowestCommonAncestor(tree,7,12).val)
