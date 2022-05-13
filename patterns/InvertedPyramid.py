n = int(input("Enter no of rows :"))
i = 1 

while n>0:
  # this loop will work backwards if n=5
  # then 5 4 3 2 1
  b =1 # *variable for printing spaces
  while b<i:
    print("*",end='')
    b = b+1

