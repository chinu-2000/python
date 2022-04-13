# Tuple is a collection of data type which is
# Tuple : 0rdered , immutable , allows duplicate elements
# It is similar to a list with the main difference being
# that a tuple cant be changed after its creation
myTuple = ("alex",25,"bob")
print(myTuple)
# single element inside () arent considered as Tuples 
# they are considered as string Ex: myTuple = ("alex")
# to recognize it as tuple use a , Ex: myTuple = ("alex",)

myList = ["alex","brandon", "cane"]
myTuple2 = tuple(myList)
print(myTuple2)

# looping
myTuple = ("alex", 25, "bob")
for i in myTuple:
  print(i)

# counting
myTuple3 = ('a','b','c','b','d','e','b')
print(myTuple3.count('b'))
