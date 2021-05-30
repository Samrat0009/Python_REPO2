# The Tree Format !!

# note : most tree problems we will be using recursion !!

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#def printTree(root):                               #very simple!!
#    if root is None:              #base case!
#        return                  ##first we check if root is leaf or not! cuz then we need nod go to left or right !
#    print(root.data)
#    printTree(root.left)
#    printTree(root.right)

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


btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)
btn6 = BinaryTreeNode(6)
btn7 = BinaryTreeNode(7)


btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
btn3.left = btn6
btn3.right = btn7


printTree(btn1)

# Output :  1:L 2 | R 3 |
#           2:L 4 | R 5 |
#           4:
#           5:
#           3:L 6 | R 7 |
#           6:
#           7: