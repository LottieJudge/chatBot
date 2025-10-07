# regular function

def square(x):
  return x**2

# Lambda function
square_l = lambda x: x ** 2

print(square(4))
print(square_l(4))

#  Lambda functions generally work as arguments with higher order functions such as map(), filter() 
# Higher order functions are functions built in to python that will already do specific things to data without having to explicitly write the function.

nums = [1,2,3,4,5,6]
print(list(nums))
print(list(map(lambda x: x + 1, nums)))
# interesting!! Love map - why the heck haven't i been using this?
squared = list(map( lambda x: x**2, nums))
print(squared)

# with filter 
odds = list(filter(lambda x: x % 2 != 0, nums))
evens = list(filter(lambda x: x % 2 == 0, nums ))
print(odds, evens)

# sorted 

dict = [('Scott', 36), ('Chewie', 7),  ('Lottie', 32),  ('Watson', 9)]

by_age = sorted(dict, key=lambda x: x[1])
print(by_age)

# best practice. 
#  Use Lambda functions when you want a simple function for a short amount of time
# You're passing a simple function as the argument of a highr order function