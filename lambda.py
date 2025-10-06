# regular function

def square(x):
  return x**2

# Lambda function
square_l = lambda x: x ** 2

print(square(4))
print(square_l(4))

#  Lambda functions generally work as arguments with higher order functions such as map(), filter() 
# Higher order functions are functions built in to python that will already do specific tings to data without having to explicility write the function.