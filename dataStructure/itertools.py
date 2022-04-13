# itertools :  product , permutations ,combinations , accumulate ,groupby and infinite iteraotrs
# itertools modules is a collection of tools for handling iterators 
# simply put iterators are data type that can be used in ..for loops

# product
from ast import operator
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
print(list(prod))

# permutations : will return all possible orderings of an input
from itertools import permutations
a = [1 ,2 ,3]
perm = permutations(a)
print(list(perm))

# combinations
# function will make all possible combinations with specified length
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2)#length=2
print(comb)
print(list(comb))

# accumulate
# the accumulate function makes an iterator that returns accumulated sums
from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
print(acc)
print(list(acc))
print('**************')
acc1 = accumulate(a, func=operator.mul)
print(a)
print(list(acc1))