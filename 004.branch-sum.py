class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def branchSUm(root,sum):
    res=[]
    def branchSUmUtil(root,sum):
        if root.left is  None and root.right is None:
            res.append(sum+root.val)
        if root.left:
            branchSUmUtil(root.left,sum+root.val)
        if root.right:
            branchSUmUtil(root.right,sum+root.val)

    branchSUmUtil(root,0)
    return res

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

print(branchSUm(tree,0))