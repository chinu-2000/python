"""
____*
___**
__***
_****
*****
"""

i = 1 # i is set to 1
# as loop condition is met i<=5 , (i=1) it enters the loop
while i <=5:                    # *count no of loops

  b=1        # b is set to 1
  while b<= 5-i:                # *blank spaces
    print("_",end="") # inside the loop b<=5-1 , b<=4
    b=b+1 # as cond is TRUE _ is printed
    # b becomes 2 ... enters the loop again (while b<= 5-i:  ) 
    # this keeps on repeating untilb =4 as 4<=4
    # when b=5 loop stops

  # when above loop (child loop) terminates it enters this loop
  # j is set to 1
  j=1                           # *star printing
  # here j = 1 and (i=1) from above line 9
  # as j<=1 (1<=1) , * is printed
  # current output ____* 
  while j<=i:
    print("*",end="") 
    # j becomes 2 enters the loop again (while j<=i:)
    # as it is FALSE , 2 <=1 Loop terminates
    j=j+1
  
  # control comes to next line
  print()
  # i=2 goes to its parent loop (while i<=5):
  i=i+1


"""
____1
___22
__333
_4444
55555
"""

i = 1  
while i <= 5:                    # *count no of loops

  b = 1
  while b <= 5-i:                # *blank spaces
    print("_", end="")  
    b = b+1 

  
  j = 1                           # *sequence printing
  while j <= i:
    print(i, end="")
    j = j+1

  # control comes to next line
  print()
  # i=2 goes to its parent loop (while i<=5):
  i = i+1


"""
____1
___12
__123
_1234
12345
"""

i = 1
while i <= 5:                    # *count no of loops

  b = 1
  while b <= 5-i:                # *blank spaces
    print("_", end="")
    b = b+1

  j = 1                           # *sequence printing
  while j <= i:
    print(j, end="")
    j = j+1

  # control comes to next line
  print()
  # i=2 goes to its parent loop (while i<=5):
  i = i+1
