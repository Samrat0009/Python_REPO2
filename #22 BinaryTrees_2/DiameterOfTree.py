#Diameter of a tree is the distance between 2 farthest points!.
# i.e. in Trees Distance between two farthest nodes !!

#based on previous problems : num nodes !

# REVISION !!!!!

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Pair :
    def __init__(self, diameter, height) :
        self.diameter = diameter
        self.height = height

def diameterHelper(root) :
    if root is None :
        pair = Pair(0, 0)
        return pair
    leftPair = diameterHelper(root.left)
    rightPair = diameterHelper(root.right)

    leftDiameter = leftPair.diameter
    rightDiameter = rightPair.diameter

    diameterFromRoot = leftPair.height + rightPair.height + 1
    diameter = max(leftDiameter, rightDiameter, diameterFromRoot)
    height = max(leftPair.height,rightPair.height) + 1

    return Pair(diameter, height)

def diameterOfBinaryTree(root) :
    pair = diameterHelper(root)
    return pair.diameter


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    length = len(levelOrder)
    if length == 1 :
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root



# Main

root = takeInput()
print(diameterOfBinaryTree(root))