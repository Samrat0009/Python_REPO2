# we know stacks are LIFO structures: similar to arrays and lists!!
#
#so in general we can treat them as lists as well!

#s = [1,2,3]
#s.append(4)
#s.append(5)

#print(s.pop())
#print(s.pop())

#so we can visualise stacks as Lists : BUT !!!!!

# when we pop any item in arrays : all the elements have to shift left which creates
#                                  time complexity of : O(n)

# so we can use lists but we SHOULD NOT !!

### BUT!!!!

#To ease this : Python3 provides an inbuilt library called queue !!
#____________________________________________________________________________________________________#
import queue

q = queue.Queue()        #way to initialise q as a Queue using queue library!!
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

while not q.empty():
    print(q.get())
print()

#BUT!!!!!!! : this only follows a FIFO property unlike a stack:
#___________________________________________________________________________________________________#

#AGAIN : To ease ur pain Python3 provides a specific queue library for stacks : LifoQueue()

import queue
#inbuilt stack as lists

q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

while not q.empty():
    print(q.get())


#Explore more on the web!!

