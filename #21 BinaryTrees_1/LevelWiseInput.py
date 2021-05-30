import queue
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

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printTree(root)