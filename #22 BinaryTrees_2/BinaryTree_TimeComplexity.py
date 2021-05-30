#based on previous problems : num nodes !

# REVISION !!!!!


class BinaryNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())

    if rootData == -1:
        return

    root = BinaryNode(rootData)

    leftTree = takeInput()
    rightTree = takeInput()

    root.left = leftTree
    root.right = rightTree

    return root

def printTree(root):                      #detailed!!
    if root is None:
        return

    print(root.data,end=': ')

#    print('L', root.left.data,end=';')   : this will give error because 4/Left has no left.data !!
#    print('R',root.right.data)

    # To Fix This !!
    if root.left is not None:
        print('L ->',root.left.data,end=' | ')
    if root.right is not None:
        print('R ->',root.right.data,end='')
    print()

    printTree(root.left)
    printTree(root.right)
