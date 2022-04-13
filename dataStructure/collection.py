# collections : Counter , namedtuple , OrderedDict ,defaultDict ,deque
# collections module implements special container data types 
# and provides alternatives with some additonal functionality

# Counter
# counter is a container that stores the 
# elements as Dictionary keys and their counts as Dictionary values 

from collections import Counter
a= "aaaabbbbbccc"

my_counter =Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())


# namedtuple is an easy to create and light weight object type
from collections import namedtuple

Point = namedtuple('Point','x,y')
# this will create a class called point with 
# fields x and y
pt = Point(1,2)
print(pt)


from collections import deque
# deque is double ended queue 
# it can be used to add or remove elements
# from the both ends 

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.extendleft([4,5,6])
print(d)