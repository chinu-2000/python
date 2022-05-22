"""
LINEAR SEARCH
Linear Search is also known as sequential search
Items are searched one by one 
if the no of elements in the array i N then :Time Complexity : O(N) 
cause extra memory is not required for searching operation
we are just looping Space Complexity : O(1)
for unosrted array Linear search is good to use

*LINEAR SEARCH PSEUDOCODE
-> Create function with two parameters which are an array and a value
-> Loop through the array and check if the current array element is equal to the value
-> if it is ,  return the index at which element is found
-> if the value is never found return -1
"""
# searching algorithm - Linear Search

def linearSearch(array,value):
  # looping through the array
  for i in range(len(array)): # O(N)
    # check if the current array (array[i]) element is equal to the value
    if array[i]== value:
      return i  # return the index at which element is found
  return -1  # if the value is never found return -1
print(linearSearch([20,40,30,50,90],50)) # OP - 3


# without comments


def linearSearch(array, value):
  for i in range(len(array)):
    if array[i] == value:
      return i  
  return -1

print(linearSearch([20, 40, 30, 50, 90], 50))
