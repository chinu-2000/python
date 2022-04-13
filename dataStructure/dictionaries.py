# Dictionary is a collection data type that is  
# Dictionary :key-value pairs , unordered , mutable
# it has a collection of key-value-pairs so each key value 
# pair match the key to its associated value
# Dictionary is mutable so we can add or change items 
# List cannot be used as a key

myDict = {"name" : "Max" , "age" : 28 , "city" : "New York" }
print(myDict)

myDict2 = dict(name="Mary",age="23",city="LA")
print(myDict2)

value = myDict["name"]
print(value)

# adding elements
myDict["email"] = "max@outlook.com"
print(myDict)

#deleting
del myDict["email"]
print(myDict)

myDict.pop("age")
print(myDict)

# Looping
for key in myDict:
  print(key)

#D.values() -> an object providing a view on D's values
for value in myDict.values():
  print(value)

# addding two dictionaries
myDict3 = {"name": "Dan", "age": 25, "city": "DC" , "email" : "dan@outlook.com"}
myDict4 = {"name" : "George" , "age" : 31 , "city" : "LA" }

myDict3.update(myDict4)
print(myDict3)