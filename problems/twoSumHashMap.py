class Solution:
  def twoSum(self, nums :List[int] , target: int):
    prevMap = {} # we need a hashmap right we are gonna call it prevMap
    # every previous element is going to be stored in this map
    # we are going to be maping the value to the index of that value

    # now lets iterate through every value in the array
    # we need the index as well as the actual number 
    for i , n in enumerate(nums):
      diff = target - n   
      # checking if the difference is already in the hashmap
      # if it is then we can return the solution
      # which is going to be a pair of the indices
      if diff in prevMap: 
        return [prevMap[diff], i]
      # if we don't find the solution then we have to update our hashmap 
      prevMap[n]=i
    return