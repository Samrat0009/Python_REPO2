#For a given a Binary Tree of integers, replace each of its data with the depth of the tree.
#Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth of the given tree.



#Time complexity: O(N)
#Space complexity: O(H)
#where N is the number of nodes in the input tree
#and H is the height of the input tree

from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)

#Following is the structure used to represent the Binary Tree Node

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def changeToDepthTreeHelper(root, level) :
    if root is None :
        return
    root.data = level
    changeToDepthTreeHelper(root.left, level + 1)
    changeToDepthTreeHelper(root.right, level + 1)
def changeToDepthTree(root) :
    changeToDepthTreeHelper(root, 0)
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
def inOrder(root) :
    if root is None :
        return
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)
# Main
root = takeInput()
changeToDepthTree(root)
inOrder(root)