# Map() - Map is a built in function that works likes a for loop, applying a given set of instructions to each item in an iterable and returns the new iterable. 

#  Syntax:  map(function, iterable, [iterable2, iterable3])

def double(x):
  return x * 2

nums = [1, 2, 3, 4, 5, 8]

dubbed = map(double, nums)
print(list(dubbed)) #Use list to be able to print out the results 

def squared(x):
  return x ** 2

sqd = map(squared, nums)
print(list(sqd))

# Using map() with built in functions. 