class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root,res):
    if root is None:
        return
    inorder(root.left,res)
    res.append(root.val)
    inorder(root.right,res)
    return res

def preorder(root,res):
    if root is None:
        return
    res.append(root.val)
    preorder(root.left,res)
    preorder(root.right,res)
    return res

def postorder(root,res):
    if root is None:
        return
    postorder(root.left,res)
    postorder(root.right,res)
    res.append(root.val)
    return res



tree = Tnode(5)
tree.left = Tnode(2)
tree.right = Tnode(9)
tree.left.left = Tnode(1)
tree.left.right = Tnode(3)
tree.right.left = Tnode(7)
tree.right.right = Tnode(12)

print(preorder(tree,[]))
print(postorder(tree,[]))
print(inorder(tree,[]))
