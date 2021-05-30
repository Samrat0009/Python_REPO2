#  FORGET IT !!!!!!!!!!!!!!!!!


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
            head = newNode                          #(consider head as a pointer for understanding)
        else:
            current = head
            while current.next is not None:     #### we move forward in list till current.next is None !!!!!
                current = current.next          # or we can say : we keeps traversing in the list till current.next........ !

            current.next = newNode                 # points to the reference of next node!

    return head

head = takeInput()
