# linkedList : Each element of the list has a connection with one another i.e. "they are linked"
#            : Each element in LL is called a "node" !!

# Node stores 2 things : 1. Data
#                        2. Reference to the next node !!

# let elements and their reference in a list be :(Data,reference)
#                                                 1,200
#                                                 5,100
#                                                 4,300
#                                                 3,900
#                                                 2,500



# Way To store a Linked List : (Data,reference to the next node)
# Node 1 : (1,100)                        : here 100 is reference of (data=5)
# Node 2 : (5,300)
# Node 3 : (4,900)
# Node 4 : (3,500)
# Node 4 : (2,none)                      'none' : since there is no next node !


# Head of the Linked List : reference to the 1st node !
#                         : stores the initial reference (200) in this case!
#                         : you can traverse the whole LL only if you have the head of the LL

# Tail of the Linked List : last Node of the LL !!