
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

# Use recursion (induction Hypothesis) !!
def Reverse(head) :
    if head is None or head.next is None:
        return head

    newHead = Reverse(head.next)  # this means get Reverse of rest of the list! then again and again n again ....

    tail = newHead                         #curr will help to run till the length of LL !!
    while tail.next is not None:
        tail=tail.next
    tail.next = head                         #tail will become new Head !
    head.next = None                         # and next of tail should be 1st element so tail.next=head

    return newHead




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
head = Reverse(head)
printLinkedList(head)

