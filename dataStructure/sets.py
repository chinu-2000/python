# sets : is a collection datatype
# sets : unordered ,mutable ,no duplicates
# unlike list and tuples it does not allow duplicates

myset = {1,2,3}
print(myset)
myset2 = {1,2,3,1,2}
print(myset2)

# the printed order will be arbitary cause set is unordered 

myset3 = set("Hello") 
print(myset3)

# looping
myset = {1, 2, 3}
for i in myset:
  print(i)

# adding Union method is only available over Sets.
odd = {1,3,5,7,9}
even = {0,2,4,6,8,10}
prime = {2,3,5,7}
u = odd.union(even)
print(u)
i = odd.intersection(prime)
print(i)