# strings : ordered , immutable , text representation

my_string = "Hello World"
print(my_string)

# looping
my_string = "Hello World"
for i in my_string:
  print(i)

# misc
my_string = "Hello World"
print(my_string.find('e'))
print(my_string.count('l'))
print(my_string.split())
#['Hello', 'World']

# formatting ---- OLD
var1 = "sam"
my_string1 = "How you doing ? %s" %var1
print(my_string1)

var2 = 2
my_string2 = "What is one +one ? %d" %var2
print(my_string2)

# formatting ---- NEW
var1 = "sam"
var2 = 2
my_string1 = "How you doing ? {} and {}".format(var1 , var2)
print(my_string1)

# formatting ---- LATEST : f-strings
var1 = "sam"
my_string1 = f"How you doing {var1} and {var2}? "
print(my_string1)
