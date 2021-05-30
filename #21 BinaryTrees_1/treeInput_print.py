# The Tree Format !!

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):                      #detailed!!
    if root is None:
        return

    print(root.data,end=': ')

    if root.left is not None:
        print('L ->',root.left.data,end=' | ')
    if root.right is not None:
        print('R ->',root.right.data,end='')
    print()

    printTree(root.left)
    printTree(root.right)

def treeInput():                         # codeZen/hacker-earth takes input in different way (level wise)
    rootData = int(input())

    if rootData == -1:                 # base case
        return None

    root = BinaryTreeNode(rootData)

    leftTree = treeInput()                #this just defines leftree,righttree
    rightTree = treeInput()               # does not call (recurse) the function treeInput()

    root.left = leftTree                  # here the function will be called
    root.right = rightTree

    return root

root = treeInput()
printTree(root)

# EXAMPLE :

#INPUT:

# 1
# 2
# 4
# -1
# -1
# 5
# -1
# -1
# 3
# -1
# 7
# -1
# -1

#OUTPUT:

# 1: L -> 2 | R -> 3
# 2: L -> 4 | R -> 5
# 4:
# 5:
# 3: R -> 7
# 7: