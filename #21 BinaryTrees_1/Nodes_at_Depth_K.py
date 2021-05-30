# if you say print at depth 1 then it will print every node under the first node!!
# 0 : L 2, R 3
# 2 : L 4, R 5 ,etc.....
# it will print everything at depth 1 i.e. everything under 0 !!

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

def printDepthk(root,k):
    if root is None:
        return

    if k==0:
        print(root.data)
        return

    printDepthk(root.left,k-1)
    printDepthk(root.right,k-1)

# Another way :

def printDepthk_V2(root,k,d=0):
    if root is None:
        return

    if k==d:
        print(root.data)
        return

    printDepthk_V2(root.left,k,d+1)
    printDepthk_V2(root.right,k,d+1)


root = treeInput()
printTree(root)
printDepthk_V2(root,2)



#1
#2
#4
#-1
#-1
#5
#-1
#-1
#3
#6
#-1
#-1
#-1


#1: L -> 2 | R -> 3
#2: L -> 4 | R -> 5
#4:
#5:
#3: L -> 6 |
#6:

# Three nodes at level 2 !!
#4
#5
#6
