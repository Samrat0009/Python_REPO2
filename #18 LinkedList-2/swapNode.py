class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
    if head is None:
        return head
    if i==j:
        return head

    head1 = head
    count=0
    while head is not None:
        if count==i:
            tempi = head
        if count==j:
            tempj = head
        count+=1
        head=head.next

    printll(tempi)
    printll(tempj)
    count =0
    while head1 is not None:
        if count == i:
            print(tempj.data,end=" ")
            head1=head1.next
        if count == j-1:
            print(tempi.data,end=" ")
            head1=head1.next
        if head1 is None:
            return
        count+=1
        print(head1.data,end=" ")
        head1=head1.next

    return

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
x, y=list(int(i) for i in input().strip().split(' '))
if x>=y:
    i=y
    j=x
else:
    i=x
    j=y
l = swap_nodes(l, i, j)
printll(l)
