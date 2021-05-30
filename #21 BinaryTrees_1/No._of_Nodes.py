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

    leftTree = treeInput()
    rightTree = treeInput()

    root.left = leftTree
    root.right = rightTree

    return root

def numNodes(root):
    if root is None:
        return 0

    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)

    return 1 + leftCount + rightCount

root = treeInput()
printTree(root)
print(numNodes(root))