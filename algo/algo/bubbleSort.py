def bubbleSort(customList):
  for i in range ((len(customList))-1):                     
    for j in range ((len(customList))-i-1):                 
      if customList[j]>customList[j+1]:                     
        customList[j] , customList[j+1] = customList[j+1] , customList[j]    
  print(customList)

cList = [13,12,14,6,9,2,8]
bubbleSort(cList)
