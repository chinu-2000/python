def insertionSort(customList):
  for i in range( 1 , len(customList)): 
    key = customList[i] 
    j = i-1

    while j >= 0 and key <= customList[j]: 
      customList[j+1] = customList[j] 
      j = j-1
    customList[j+1] = key         
  print(customList)

cList = [13, 12, 14, 6, 9, 2, 8]
insertionSort(cList)
