# Basically we remove Traversal within the list!!

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
        return head,head

    smallHead,smallTail = Reverse(head.next)        # Let linked List be 1->2->3->4->5->6->7->8->9->None
    head.next = None                                # so initially : head is pointing to 1
    smallTail.next=head                             #   and        : 9.next = None
                                                    # now what head.next=None does here is  : 1.next = None
                                                    # and smallTail.next=head does is       : smallTail.next = 1   (because 1 was head)
                                                    # in total logic                        : smallTail->1->None    (here 1 was still head so..)
                                                    #                                       : smallTail->2->1->None (because now 2 became head : when function is recalled for smallhead)
                                                    #                                       : smallTail->3->2->1->None (now 3 became head)
                                                    # and so on................................
    return smallHead,head


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
head,tail = Reverse(head)
printLinkedList(head)

