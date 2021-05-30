#For a given a Binary Tree of type integer, duplicate every node of the tree and attach it to the left of itself.
#The root will remain the same. So you just need to insert nodes in the given Binary Tree.


10/19/2020 Coding Ninjas
https://classroom.codingninjas.com/app/classroom/me/1805/content/31530/offering/335839/problem/512 1/2
'''
Time complexity : O(N)
Space complexity : O(H)
where N is the number of nodes in the tree
and H is the height of the tree.
H is equal to log(N) for a balanced tree
'''
from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)
#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
def __init__(self, data):
self.data = data
self.left = None
self.right = None
def insertDuplicateNode(root):
if root is None :
return
newNode = BinaryTreeNode(root.data)
rootLeft = root.left
root.left = newNode
newNode.left = rootLeft
insertDuplicateNode(rootLeft)
insertDuplicateNode(root.right)
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
10/19/2020 Coding Ninjas
https://classroom.codingninjas.com/app/classroom/me/1805/content/31530/offering/335839/problem/512 2/2
rightChild = levelOrder[start]
start += 1
if rightChild != -1:
rightNode = BinaryTreeNode(rightChild)
currentNode.right =rightNode
q.put(rightNode)
return root
def printLevelWise(root):
if root is None:
return
inputQ = queue.Queue()
outputQ = queue.Queue()
inputQ.put(root)
while not inputQ.empty():
while not inputQ.empty():
curr = inputQ.get()
print(curr.data, end=' ')
if curr.left!=None:
outputQ.put(curr.left)
if curr.right!=None:
outputQ.put(curr.right)
print()
inputQ, outputQ = outputQ, inputQ
# Main
root = takeInput()
insertDuplicateNode(root)
printLevelWise(root)