# leaf nodes are nodes that only have a parent no child!!
# that is : if left and right are none : root contribution =1

# The Tree Format !!

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def numLeafNodes(root):
    if root is None:
        return 0                                            # 2 base cases!
    if root.left == None and root.right == None:
        return 1

    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)

    return numLeafLeft + numLeafRight

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

    leftTree = treeInput()
    rightTree = treeInput()

    root.left = leftTree
    root.right = rightTree

    return root

root = treeInput()
printTree(root)
print(numLeafNodes(root))

# Input :

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


# Output = 3