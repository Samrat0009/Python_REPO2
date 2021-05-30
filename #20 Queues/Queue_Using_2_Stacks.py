# here 1 of dequeue or enqueue can be O(n).
# Note : queues are FIFO nad stacks are LIFO !!

class QueueUsingTwoStacks:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def enqueue(self, data):
        while len(self.q1) != 0:
            self.q2.append(self.q1.pop())

        self.q1.append(data)

        while len(self.q2) != 0:
            self.q1.append(self.q2.pop())

        return

    def dequeue(self):

        if len(self.q1) == 0:
            return -1

        return self.q1.pop()

    def front(self):

        if len(self.q1) == 0:
            return -1
        return self.q1[-1]

    def size(self):
        return len(self.q1)

    def isEmpty(self):
        return self.size() == 0


s = QueueUsingTwoStacks()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.enqueue(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.dequeue()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.front()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.size())
    elif choice == 5:
        while len(s.q1) != 0:
            print(s.q1.pop(), end=' ')

    i += 1