class QueueUsingArray:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enqueue(self,data):
        self.__arr.append(data)
        self.__count+=1

    def dequeue(self):

        if self.__count == 0:
            return -1

        element = self.__arr[self.__front]            #no matter what the count is front will always start from 0, so
        self.__front+=1                               #so FIFO will be followed i.e. : first is printed first because of front !!
        self.__count-=1
        return element

    def front(self):
        if self.__count==0:
            return -1

        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):

        return self.size() == 0

q = QueueUsingArray()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.size())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1