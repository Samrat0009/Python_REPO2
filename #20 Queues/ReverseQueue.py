#______________________________REDO____________________________________!!

#this solution is totally wrong !!

# Note : queues are FIFO nad stacks are LIFO !!

class Stack:
    def __init__(node):
        node.data = []

    def Empty(node):
        return node.data == []

    def push(node, data):
        node.data.append(data)

    def pop(node):
        return node.data.pop()


class Queue:
    def __init__(node):
        node.data = []

    def Empty(node):
        return node.data == []

    def enQueue(node, data):
        node.data.insert(0, data)

    def deQueue(node):
        return node.data.pop()


def Reverse():
    while (not Q.Empty()):
        S.push(Q.deQueue())
    while (not S.Empty()):
        Q.enQueue(S.pop())

S = Stack()
Q = Queue()

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split())[1:]]
for ele in li:
    Q.enQueue(ele)
i=0
while i < len(li):
    print(Q.data[i],end=' ')
    i+=1


