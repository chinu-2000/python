"""
BINARY SEARCH
-> binary search is faster than linear search
-> half of the remaining elements can be eliminated at a time ,
  instead of eliminating them one by one
-> binary search works only for sorted array

1 2 3 4 5 6 7 8 9  | value we are looking for - 6
spot the middle element in the array (5)
we check if the value we are looking for (6) is
greater or smaller than the middle element (5)
as the value (6) is greater than the middle element(5)
we eliminate all the elements located on the 
left of middle element including 5
new array - 6 7 8 9
middle element - 7
6 < 7  
we eliminate all the elements located on the 
left of middle element including 7
we get 6
"""
"""

*BINARY SEARCH PSEUDO CODE
-> create function with two parameters which are sorted array and a value
-> create two pointers : 
a left pointer at the start of the array
a right pointer at the end of the array
-> based on right and left pointers calculate the middle pointer

-> While middle is not equal to the value and start<=end loop:
    --> if the middle is greater than the value move the right pointer down
    --> if the middle is less than the value move the left pointer up
-> if the value is never found return -1

"""
import math
def binarySearch(array , value):
  # creating pointers 
  start = 0 # left pointer
  end = len(array)-1 # end of array | index of python starts with 0
  # *middle pointer
  middle = math.floor((start+end)/2)
  print(start,middle,end)

  while not(array[middle] == value ) and start<=end:
    if value < array[middle]:
      end = middle -1
    else:
      start =middle +1
    middle = math.floor((start+end)/2)
    print(start , middle ,end)
# if we dont wwrite this loop and the condition start<=end the loop will
# work infinitely for a number which does not exist in the array
  if array[middle] == value:
    return middle 
  else :
    return -1

customArray = [8, 9 , 12 , 15 , 17 , 19 , 20 , 21 , 28]
print(binarySearch(customArray , 15))


"""
8, 9, 12, 15, 17, 19, 20, 21, 28
S             M                E
if the value we are looking for 15 in this case
is less than the middle pointer 17 in this case
so we need to move our end pointer (E) to => end = middle -1
else : if no is not located at middle and no is greater than middle
we need to move our start position (S) to => start =middle +1
OUTPUT
0 4 8
0 1 3
2 2 3
3 3 3
3

BINARY SEARCH TIME COMPLEXITY 
worst and average case O(log n)
best case O(1)
"""