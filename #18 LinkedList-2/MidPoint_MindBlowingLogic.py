#basically we take 2 Pointers !!
# 1st pointer = slow : which will traverse list 1x speed
# 2nd pointer = fast : which will traverse list 2x speed



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
def midPoint(head):

    #fastP = head
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    print(slow.data)












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
head = midPoint(head)
printLinkedList(head)

