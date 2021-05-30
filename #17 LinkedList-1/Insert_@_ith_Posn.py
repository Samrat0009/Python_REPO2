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

def insertLL(head,data,i):
    count = 0
    if i<0 or i>length(head):
        return head

    prev = None
    curr = head

    while count<i:

        prev = curr
        curr = curr.next
        count+=1

    newNode = node(data)

    if prev is not None:
        prev.next = newNode
    else:
        head = newNode

    newNode.next = curr

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
    insertLL(head, data, i)
    printLL(head)

    t -= 1