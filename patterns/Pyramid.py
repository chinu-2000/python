"""
____*
___***
__*****
_*******
*********  
"""
"""
Number of 
SPACES | STARS
_ 4       1
_ 3       3
_ 2       5
_ 1       7
_ 0       9
We will make two loops one for spaces ...one for stars
How the variables are acting :
k = 1 3 5 7 9 
i = 1 2 3 4 5
b = 1
j = 1 2 3 4
"""
k = 1 
i = 1 # k and i are set to 1 
# cond (while i<=5:) is TRUE as (1 <= 5) 
while i<=5:                       #*parent 
# * S P A C E     P R I N T I N G
  b = 1 # b is set to 1
  while b<= 5-i:                  #*child 1
    # for the loop in child 1 (b<= 5-i) :
    # where i =1 is TRUE ... 1 <=4 Hence 
    print("_" , end = "") # space is printed 
    b = b+1 # loop is repeated four times until condition turns FALSE

# * S T A R     P R I N T I N G
  j = 1 # j is set to 1
  while j <= k:                   # *child 2
    # for the loop in child 2 ( while j <= k:):
    # j =1 and k =1 Hence j <= k , (1<=1) is True
    print("*" , end = "") # star is printed 
    j = j+1 # one time as ... if loop repeates condition turns FALSE

  k = k+2 # initial working value of k is incremented from k =1 => k =3
  print() # Output cursor moves to next line
  i = i+1 # value of i is incremented from i =1 => i =2 
  # *Now it goes back to its parent loop

"""
____1
___333
__55555
_7777777
999999999
"""
k = 1
i = 1
while i<=5:

  # * S P A C E     P R I N T I N G
  b = 1
  while b<= 5-i:
    print("_" , end = "")
    b = b+1

  # * N U M B E R    P R I N T I N G
  j = 1
  while j<=k:
    print(k , end = "")
    j = j+1

  k = k+2
  print()
  i = i+1

"""
____1
___222
__33333
_4444444
555555555
"""
k = 1
i = 1
while i <= 5:

  # * S P A C E     P R I N T I N G
  b = 1
  while b <= 5-i:
    print("_", end="")
    b = b+1

  # * N U M B E R     P R I N T I N G
  j = 1
  while j <= k:
    print(i, end="")
    j = j+1

  k = k+2
  print()
  i = i+1

"""
____1
___123
__12345
_1234567
123456789
"""
k = 1
i = 1
while i <= 5:

  # * S P A C E     P R I N T I N G
  b = 1
  while b <= 5-i:
    print("_", end="")
    b = b+1

  # * N U M B E R     P R I N T I N G
  j = 1
  while j <= k:
    print(j, end="")
    j = j+1

  k = k+2
  print()
  i = i+1
