from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    length = 0

    while head is not None:
        length += 1
        head = head.next

    return length


def deleteNode(head, i):
    if i < 0 or i >= length(head):
        print(head.data, end=" ")
        head = head.next

    arr = []
    if i == 0:
        head = head.next
        arr.append(head.data)

    count = 0
    while head is not None:
        count += 1
        if count == i:
            print(head.data, end=" ")
            cur = head.next
            head = cur.next
        else:
            print(head.data, end=" ")
            head = head.next
    print()
    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    i = int(stdin.readline().rstrip())

    deleteNode(head, i)

    t -= 1