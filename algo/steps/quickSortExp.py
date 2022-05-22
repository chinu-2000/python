# we take pivot element as the right most element
# so pivot = customList[high]
# quick sort is a divide and conquer algorithm
# find pivot number and make sure
# smaller numbers located at the left of pivot
# and bigger numbers are located at the right of the pivot
# unlike mergeSort extra space is not required
"""
When to use QuickSort :
-> When average expected time is O(NlogN)
When to avoid Quick Sort :
-> When Space is a concern
-> When you need stable sort
"""
# *fastest
# *partition function : O(n) Time Complexity
# *Time Complexity QuickSort : O(nLogN)
# *Space Complexity : O(n) cause we are calling quickSort recursively
# *When we call a methid recursively it occupies place in stack memory
# *low -low which is the first index
# *high - high which is the second index


def partition(customList, low, high):
  #  we create a variable i
  # we will use this inside loop when we will swap the values
  i = low - 1
  pivot = customList[high]  # O(1)
  # loop for swapping elements
  for j in range(low, high):  # O(n)
    if customList[j] <= pivot:
      i = i+1
      customList[i], customList[j] = customList[j], customList[i]
  # if this is not the case then outside the loop we will replace the value
  # which is bigger than the pivot with pivot values : customList[high] = pivot
  customList[i+1], customList[high] = customList[high], customList[i+1]  # O(1)
  return (i+1)  # O(1)


def quickSort(customList, low, high):  # low - starting index | high - ending index
  if low < high:
    # O(n) cause partition function takes O(n) TC
    pi = partition(customList, low, high)
    # pi - partition index which will come from partition function
    quickSort(customList, low, pi-1)  # we call quickSort #T(n/2)
    quickSort(customList, pi+1, high)  # T(n/2)


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
quickSort(cList, 0, 8)
print(cList)
