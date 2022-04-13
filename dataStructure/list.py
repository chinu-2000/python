# List is a collection of data type which is
# List : 0rdered , mutable , allows duplicate elements 
myList = ["alex","brandon", "cane"]
print(myList)

# list allows different data types
myList2 = ["alex" ,"a" , 1 , True]
print(myList2)

# Looping
if "alex" in myList:
  print("yes")
else:
  print("no")

#length
print(len(myList))

#append ,remove
myList.append("lemon")
print(myList)

myList.insert(1,"orange")
print(myList)

myList.remove("orange")
print(myList)

#sort
myList3 = [3,5,7,1,2,8,5]
# myList3.sort()
print(myList3)

new_myList3 = sorted(myList3)
print(new_myList3)

#adding 2 list
myList4 = myList2 + myList3
print(myList4)

