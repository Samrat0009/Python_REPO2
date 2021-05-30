

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    length = 0

    while head is not None:
        length+=1
        head = head.next

    return length

def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if (h1.data < h2.data):
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h2.next, h1)
        return h2


def mergeSort(head):
    if head is None or head.next is None:
        return head

    mid = length(head)//2

    count = 0
    head1 = Node(head.data)
    while head is not None:
        if count<mid:
            head1.next = head
            count+=1
        else:
            break
        head = head.next

    while head is not None:
        head2 = head


        return printLinkedList(head1),printLinkedList(head2)
    #mergeSort(head1)
    #mergeSort(head2)

    #return  merge(head1,head2)





#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()



head = takeInput()
head = mergeSort(head)
printLinkedList(head)
