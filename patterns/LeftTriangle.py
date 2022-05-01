"""
* 
**
***
****
*****
"""
i = 1                      # i is set to 1
while i <= 5:               # cond is checked it enters loop's body
  j = 1                    # j is set to 1
  while j <= i:           # loop is correct , TRUE
    # * is printed cursor does not move to next line as end = ''
    print('*', end='')
    j = j+1                  # * j =2 as j is incremented ... while loop returns FALSE
  print()                  # next line starts ... o/p cursor enters second line
  # * value of i increments to 2 ... goes back to ...while i<=5 ... j becomes 1 again
  i = i+1


"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""
i = 1                      
while i <= 5:              
  j = 1                    
  while j <= i:           

    print(i, end='') # i increments in each line
    j = j+1                  
  print()                 

  i = i+1           # i increments in each line


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
i = 1
while i <= 5:
  j = 1
  while j <= i:

    print(j, end='')  # i increments in each line
    j = j+1
  print()

  i = i+1           # i increments in each line


