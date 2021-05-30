#while taking input : when the hed points to the 2nd element : O(1) work is done.
#                similarly while pointing to the 3rd element : O(2) work is done
#                                                               .
#                                                               .
#                                                               .
#                                                               .
#                  for n elements of input for a linked list : O(n-1) work is done.


# Time Complexity = Summation of work = n(n-1)/2 = (n^2-n)/2 = O(n^2) : which is not ideal !!


# NOTE : The only thing taking time in the code is traversing through the input array !!

# SOLUTION : Stop Traversing !!

# EXP : We maintain a last element of LL known as ' TAIL ' !!!


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    inputlist = [int(ele) for ele in input().split()]
    head = None                           # this is if no input is there it will return none !
    tail = None
    for element in inputlist:             #iterating in the list!
        if element==-1:
            break

        newNode = node(element)            # this creates the nodes up till data is '-1'

        if head is None:
            head = newNode                         #(consider head as a pointer for understanding)
            tail = newNode
        else:
            tail.next = newNode                # points to the reference of next node!
            tail = newNode                     # shifts tail to the latest node !!
    return head

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next                         # ex : node1.next=node2 then node2.next=node3........so on..
    print("none")

list = takeInput()
printLL(list)