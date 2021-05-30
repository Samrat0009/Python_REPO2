class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# so we take input like 1, 2, 3, 5, 6, 7, -1 till '-1' !!

def takeInput():
    inputlist = [int(ele) for ele in input().split()]
    head = None                           # this is if no input is there it will return none !
    for element in inputlist:             #iterating in the list!
        if element==-1:
            break

        newNode = node(element)            # this creates the nodes up till data is '-1'

        if head is None:
            head = newNode
        else:                                  ## this is for storing the rest of the elements
            current = head
            while current.next is not None:
                current = current.next                # curr keeps traversing in the list !
            current.next = newNode                 # points to the reference of next node!

    return head

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next                         # ex : node1.next=node2 then node2.next=node3........so on..
    print("none")

head = takeInput()
printLL(head)                 # main.head
printLL(head)                # since here, above LL points to None so head remains same !!
# this is different from above print!!