""" Pascals Triangle
In Pascal's Triangle , each number is the sum of the two numbers directly above it
Time Complexity & Space Complexity O(n^2)
n - num of rows
We are gonna have n different rows each row can have a size upto n
"""
# *By default input function will take char as an input so use int(input())
"""
Think of the problem as an a stair of array
      [1] 
    [1 ,1]  
  [1 ,2 ,1]

for simplicity :
    [0 ,1 ,0]
  [0 ,1 ,1 ,0]

  [0,1 ,2 ,1 ,0]
  [1 ,3 ,3 ,1]
"""
class Solution :

  def generate(self ,numRows : int):
    res = [[1]] # result res=1 base case

    # for building rows
    for i in range(numRows - 1): 
      temp = [0] + res[-1] + [0]
      row = []
      # building next rows
      # length of next row = len of previous row +1
      for j in range(len(res[-1])+1):
        row.append(temp[j] + temp[j+1])
      res.append(row)
    return res

"""
1     for i = 0
11    for i = 1
121   for i = 2
1331  for i = 3
14641
"""

# each row is inner list of list 1
# inner list name is temp_list in each iteration
n = int(input("enter the row number : "))
list1 = []
for i in range(i+1) : # no of rows
  temp_list = []
