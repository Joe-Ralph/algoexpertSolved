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


def insert(root,val):
    if root is None:
        root = Tnode(val)
    elif val < root.val:
        root.left = insert(root.left,val)
    elif val > root.val:
        root.right = insert(root.right,val)
    return root

minim = float('inf')

def findClosestValue(root,val):
    global minim
    if root is None:
        return root
    elif val < root.val:
        if abs(val - minim) > abs(val - root.val): minim = root.val
        findClosestValue(root.left,val)
    elif val > root.val:
        if abs(val - minim) > abs(val - root.val): minim = root.val
        findClosestValue(root.right,val)
    else: 
        minim = root.val


tree1 = None
tree1 = insert(tree1,10)
tree1 = insert(tree1,5)
tree1 = insert(tree1,15)
tree1 = insert(tree1,2)
tree1 = insert(tree1,5)
tree1 = insert(tree1,13)
tree1 = insert(tree1,22)
tree1 = insert(tree1,1)
tree1 = insert(tree1,14)
# inorder(tree1)
findClosestValue(tree1,12)
print(minim)