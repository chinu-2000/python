# divide the given array into two part
# take first element from unsorted array and find its correct
# position in sorted array
# repeat until unsorted array is empty

def insertionSort(customList):
  # here range starts from 1 cause we will compare
  # current element with the next element which is at index 1
  for i in range(1, len(customList)):  # -------->O(n)
    # i --> current variable
    key = customList[i]  # key --> variable  #-------->O(1)
    j = i-1  # previous element

    while j >= 0 and key <= customList[j]:  # -------->O(n)
      # here we swap current element with the next element
      # current element = customList[j+1] we added 1 here cause
      # we assigned j = i-1
      customList[j+1] = customList[j]
      j = j-1
      # we need to decrease j by 1 each time cause we will take previous
      # element .. if we dont put this cond here then it will run infinitely
      # if the condition is not met
    customList[j+1] = key
    # we assign key to customList[j+1]
  print(customList)


cList = [13, 12, 14, 6, 9, 2, 8]
insertionSort(cList)

# TimeComplexity  --> O(n^2)
# SpaceComplexity --> O(1)
