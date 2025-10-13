def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  if(size == 'a'):
    size = 'Small'
  elif(size == 'b'):
    size = 'Medium'
  elif(size == 'c'):
    size = 'Large'
  else:
    print_message()
    get_size()
  print(size)

def get_size():
  res = input("What size drink would you like? \n[a] small \n[b] medium \n[c] large \n")
  return res.lower()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

coffee_bot()