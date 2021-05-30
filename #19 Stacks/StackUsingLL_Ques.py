###Following Node class us already created internally. You can directly use that.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLL:
    def __init__(self):
        self.__head = None
        self.__count = 0


    def push(self, item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1


    def pop(self):
        if self.isEmpty() is True:
            print('stack is empty')
            return

        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1

        return data


    def top(self):
        if self.isEmpty() is True:
            print('stack is empty')
            return

        data = self.__head.data
        return data


    def size(self):
        return self.__count


    def isEmpty(self):
        return self.size() == 0


s = StackUsingLL()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.size())
    elif choice == 5:
        if (s.isEmpty()):
            print('true')
        else:
            print('false')
    i += 1






