def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  if(size == 'a'):
    size = 'Small'
  elif(size == 'b'):
    size = 'Medium'
  elif(size == 'c'):
    size = 'Large'
  print(size)

def get_size():
  res = input("What size drink would you like? \n[a] small \n[b] medium \n[c] large \n")
  return res

coffee_bot()