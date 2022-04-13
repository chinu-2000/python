# data+next = node
# every next of each node points to next node
# last node --> next == null
# start => node1 => node2
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None ; 

class LinkedList:
  
  def __init__(self):
    self.start = None;
  
  # value : data to be inserted
  def insertLast(self, value):
    # now as we want to insert a new node 
    # we have to make an object of the node : node()
    # as we did create a node we have to pass data to it
    newNode =  Node(value) # for referring to this we create variable : newNode
    
    if(self.start == None): # Linked List is empty
      self.start = newNode ;
    else:
      # variable for traversing
      temp  =self.start # now temp points to firstNode
      while temp.next != None:
        temp = temp.next # temp.next = second node
      temp.next = newNode # here we insert  new node

# in python if there is nothing pointing to a memory block
# python erases it on its own
  def deleteFirst(self ):
    if (self.start == None):
      print("e m p t y")
    else :
      # we have to remove first node
      temp = self.start # temp has the value of first node :deleted
      # the reference of second node is placed inside start
      # now start reference to second node : start --> second node
      self.start = self.start.next

  def viewList(self):
    if (self.start == None):
      print("e m p t y")
    else :
      temp = self.start # first node reference is stored inside temp
      while temp!= None:
        print(temp.data , end = ' ')
        temp = temp.next


myList = LinkedList()
myList.insertLast(10)
myList.insertLast(20)
myList.insertLast(30)
myList.viewList()
print()
myList.deleteFirst()
myList.viewList()




