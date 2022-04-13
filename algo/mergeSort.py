# bubble sort :  we repeatedly compare each pair of adjacent items
# and swap them if they are in wrong order
# every pair is compared and swapped if necessary

def bubbleSort(customList):
  for i in range ((len(customList))-1):                     #O(n)
    # -i -1 cause here we will compare adjacent elements    
    for j in range ((len(customList))-i-1):                 #O(n)
      if customList[j]>customList[j+1]:                     #O(1)
        # swapping                                          #O(1)
        customList[j] , customList[j+1] = customList[j+1] , customList[j]  
  
  print(customList)


cList = [13,12,14,6,9,2,8]
bubbleSort(cList)

# time complexity O(n^2)
# space complexity O(1) - as extra space is not required