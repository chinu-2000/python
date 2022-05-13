def insertionSort(customList):
  for i in range(1, len(customList)): 
    key = customList[i]
    j = i-1 
    while j >= 0 and key <= customList[j]: 
      customList[j+1] = customList[j]
      j = j-1
    customList[j+1] = key
  return customList
# *----------------------------------------------------------
# * B U C K E T S O R T
# *----------------------------------------------------------
# create buckets and distribute elements of array into buckets
# sort buckets individually
# merge buckets after sorting

# *no of buckets  = round(sqrt(number of elements))
# after getting the value of number of buckets
# we have to find out which no goes in which bucket
# *appropriate bucket = ceil(Value * number of buckets / maxValue) 

import math

def bucketSort(customList):
  numberOfBuckets = round(math.sqrt(len(customList)))
  max_value = max(customList)
  arr = []  # temp array

  # creating buckets
  for i in range(numberOfBuckets):
    arr.append([]) # sub-array
  # after creating our bucket we will insert different elements from this
  # custom list to these buckets ... for this we have to look through all elemnets 
  # of these custom ... based on the formula we need to find our index of the bucket that 
  # we are going to insert measured element
  for j in customList:
    index_b = math.ceil(j*numberOfBuckets/max_value)
    # -1 cause index starts from zero
    # we are inserting the elements to the appropriate bucket
    arr[index_b-1].append(j)     
# after inserting all elements in the appropriate bucket , we need to sort them So : 
  for i in range(numberOfBuckets):
    arr[i] = insertionSort(arr[i])
  # now we need to merge the buckets
  k = 0 # temp value
  for i in range(numberOfBuckets):
    for j in range(len(arr[i])):
      customList[k] = arr[i][j]
      k = k+1
  return customList


cList = [13, 12, 14, 6, 9, 2, 8]
print(bucketSort(cList))
