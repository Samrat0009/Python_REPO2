#PostOrder : root is printed last (reverse Traversal)
#InOrder : root is printed first (forward Traversal)
#PreOrder : we have already Done
#LevelOrder : also Done !!!

#PreOrder
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if root is None:
        return

    print(root.data,end=' ')

    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)

    print(root.data,end=' ')

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

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

preOrder(root)
print()
postOrder(root)


# try: 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
#OUTPUT:
# 8 3 1 6 4 7 10 14 13
# 1 4 7 6 3 13 14 10 8