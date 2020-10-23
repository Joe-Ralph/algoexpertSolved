class Tnode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)

tree = Tnode(1)
tree.left = Tnode(2)
tree.right = Tnode(3)
tree.left.left = Tnode(4)
tree.left.right = Tnode(5)
tree.right.left = Tnode(6)
tree.right.right = Tnode(7)
maxVal = float('-inf')

def maxPathSum(root):
    global maxVal
    if not root:
        return 0
    left = maxPathSum(root.left)
    right = maxPathSum(root.right)
    ms = max(max(left,right)+root.val,root.val)
    newMs = max(left+root.val+right,ms)
    maxVal = max(maxVal,newMs)
    return ms

maxPathSum(tree)
print(maxVal)

