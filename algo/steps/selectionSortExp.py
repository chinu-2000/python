# *SELECTION SORT
"""
in case of selection sort we repeatedly find the minimum element
and move it ot the sorted part of the array to make unsorted part sorted 
# divide the array into two parts : selected and unsorted
find minimum element in the unsorted array
swap it with the first element
at the start the size of sorted array will be 1 so we will increase it every time
"""

# Time Complexity - O(n^2) Space Complexity - O(1)
"""
when to use 
-> when we have insufficient memory
When to avoid 
-> when time is of concern
[2, 12, 14, 6, 9, 13, 8]
[2, 6, 14, 12, 9, 13, 8]
[2, 6, 8, 12, 9, 13, 14]
[2, 6, 8, 9, 12, 13, 14]
[2, 6, 8, 9, 12, 13, 14]
[2, 6, 8, 9, 12, 13, 14]
[2, 6, 8, 9, 12, 13, 14]
"""
def selectionSort(customList):
  for i in range(len(customList)):      #O(n)
    min_index = i
    # i+1 cause we have to compare elements
    for j in range(i+1, len(customList)):       #O(n)
      if customList[min_index] > customList[j]: 
        # if this is true then the minimum index is not the minium
        min_index = j
        # swapping
    customList[i], customList[min_index] = customList[min_index], customList[i] #O(1)
  print(customList)

cList = [13, 12, 14, 6, 9, 2, 8]
selectionSort(cList)