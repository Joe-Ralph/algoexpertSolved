class tNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    if root is None:
        root = tNode(val)
    elif val < root.val:
        root.left = insert(root.left,val)
    elif val > root.val:
        root.right = insert(root.right,val)
    return root

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def findMin(root):
    while root.left is not None:
        root = root.left
    return root


def preorder(root):
    if root is None:
        return
    print(root.val)
    inorder(root.left)
    inorder(root.right)

def delete(root,val):
    if root is None:
        return None
    elif val < root.val:
        root.left = delete(root.left,val)
    elif val > root.val:
        root.right = delete(root.right,val)
    else:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            temp = findMin(root.right)
            root.val = temp.val
            root.right = delete(root.right,temp.val)
    return root



tree = None
tree = insert(tree,7)
tree = insert(tree,2)
tree = insert(tree,6)
tree = insert(tree,1)
inorder(tree)
print('--------------------------------------------------------------------------------')
tree = delete(tree,1)
inorder(tree)