import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def buildLevelTree(root):
    i=0
    if root is None:
        return

    node = BinaryTreeNode(root[i])
    q = queue.Queue()
    q.put(node)
    i+=1
    if not q.empty():
        currentNode = q.get()
        leftChild = root[i]






def printTree(root):

#main

root = [int(i) for i in input().split()]
buildLevelTree(root)
printTree(root)
