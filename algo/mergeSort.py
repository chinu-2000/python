# merge sort is a divide and conquer algorithm
# divide the input array in two halves and we keep halving recursively 
# until they become too small that cannot be broken further
# merge halves by sorting them 
# we have an onordered array or a list
# we divide it into 2 halves
# we further divide it into 4 halves 2 each
# we do this till the end ...until no elements are left to divide
# next step -- > we merge them in the same way we divided them

# *helper function - merge two subarrays of customList
def merge(customList , l , m , r):
  # l = first index , m = middle index , r = right index
  n1 = m - l + 1  # no of elements in first subarray
  n2 = r - m # no  elements in second subarray
# based on this no of elements we will create two  temporary arrays
  L = [0] * n1  # the first array will be L left
  R = [0] * n2  # the second array will be R right
#* now after creating these array we will copy the elements from the customList
#* to these two sub array

  for i in range(0 , n1):
    # with this we are copying the first subarrays element to first subarray
    L[i] = customList[l+i]

  for j in range(0, n2):
    # with this we are copying the first subarrays element to first subarray
    R[j] = customList[m+1+j]  
# after adding elements to these two subarrays 
# we will merge temp arrays back to customList 
# for this we create 3 var
  i =0 # initial index of first subarray
  j =0 # initial index of second subarray
  k =l  # initial index of merged subarray
  
