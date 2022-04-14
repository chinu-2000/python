# in case of selection sort we repeatedly find the minimum element 
# and move it to the sorted part of array to make unsorted part sorted
# divide the array into two parts : sorted and unsorted
# find minimum element in unsorted array 
# swap it with the first element
# at start the size of sorted array will be 1 so we will increase it 
# every time

def selectionSort(customList):
  for i in range(len(customList)):    # O(n)
    min_index = i                           
    for j in range(i+1, len(customList)):  # i+1 cause we have to compare elements # O(n)
      if customList[min_index] > customList[j]:  # O(1)
        # if this is true then minimum index is not the minimum
        min_index = j
    
    # swapping 
    customList[i] , customList[min_index] = customList[min_index] , customList[i]  # O(1)
  print(customList)


cList = [13, 12, 14, 6, 9, 2, 8]
selectionSort(cList)

# TimeComplexity  --> O(n^2)
# SpaceComplexity --> O(1)