class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    inputList = [int(x) for x in input().split()]
    head = None
    tail = None
    for element in inputList:
        if element == -1:
            return head

        newNode = node(element)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

def length(head):
    length = 0

    while head is not None:
        length+=1
        head = head.next

    return length

def insertLLR(head,data,i):

    if i<0:
        return head

    if i==0:
        newNode = node(data)
        newNode.next = head
        return newNode               # this states the new head  of the LL is now newNode

    if head is None:
        return None

    smallHead = insertLLR(head.next,data,i-1)
    head.next = smallHead

    return head

def printLL(head):
    while head is not None:
        print(head.data,end="->")
        head = head.next
    print("none")

t=1
while t > 0 :

    head = takeInput()
    i = int(input())
    data = int(input())
    head = insertLLR(head, data, i)
    printLL(head)

    t -= 1