from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    length = 0

    while head is not None:
        length+=1
        head = head.next

    return length

def isPalindrome(head):
    if length(head)==0 or length(head)==1:
        return True

    arr=[]
    while head is not None:
        arr.append(head.data)
        head=head.next

    l = int((len(arr) + 1) / 2)
    count = 0
    i = 0
    j = 1
    while (i < (l - 1)) and j <= (l - 1):
        if arr[i] == arr[-j]:
            count += 1
        j += 1
        i += 1
    if count == l - 1:
        return True
    else:
        return False


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
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1