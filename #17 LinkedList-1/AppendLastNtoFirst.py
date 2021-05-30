#You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.


from sys import stdin

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

def appendLastNToFirst(head, n) :
    if n<=0 or n>=length(head):
        return printLinkedList(head)

    k = length(head)-n

    arr = []
    while k >= 0:
        arr.append(head.data)
        head = head.next
        k -= 1
        if k==0:
            arr.append(head.data)
            break

    while head is not None:
        print(head.data,end=" ")
        head = head.next

    for i in range(len(arr)-1):
       print(arr[i],end=" ")
    print()
    return



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


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    appendLastNToFirst(head, n)

    t -= 1