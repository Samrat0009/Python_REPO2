class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

a = node(13)                 # a : 13,none      self reference = 100
b = node(15)                 # b : 15,none      self reference = 200

a.next = b                   # a : 13,None,200     (of the format: data,prev,next)
b.prev = a                   # b : 15,100,None
print(a.data)
print(b.data)
print(a.next.data)
print(b.prev.data)
# NOTE:
print(a)
print(a.next)
print(b.prev)
print(b)

#Solution for NOTE : (3rd line of o/p) : see how the reference in  node a points to reference of b !!

#<__main__.node object at 0x036CDCB0>
#<__main__.node object at 0x036D9B70>
#<__main__.node object at 0x036D9B70>

#check
print(b.next.data)

#this will show error because there is no next node !!