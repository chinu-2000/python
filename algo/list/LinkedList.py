class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.start = None

  def insertLast(self, value):
    newNode = Node(value)  
    if(self.start == None):  
      self.start = newNode
    else:
      temp = self.start 
      while temp.next != None:
        temp = temp.next  
      temp.next = newNode  

  def deleteFirst(self):
    if (self.start == None):
      print("e m p t y")
    else:    
      temp = self.start  
      self.start = self.start.next

  def viewList(self):
    if (self.start == None):
      print("e m p t y")
    else:
      temp = self.start  
      while temp != None:
        print(temp.data, end=' ')
        temp = temp.next


myList = LinkedList()
myList.insertLast(10)
myList.insertLast(20)
myList.insertLast(30)
myList.viewList()
print()
myList.deleteFirst()
myList.viewList()
