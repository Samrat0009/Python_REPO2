# main pointers: head and tail
# now since we cannot access backwards in linked list we use a diff method:

# we add values from the head side : i.e. every time you add a node prevhead = head.next and head = newNode !!


# here we need 2 new variables : head, count

from Node import Node

class stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,item):
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
        return self.size()==0