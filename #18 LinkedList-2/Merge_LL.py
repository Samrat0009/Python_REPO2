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



head1 = takeInput()
head2 = takeInput()
head = merge(head1,head2)
printLinkedList(head)
