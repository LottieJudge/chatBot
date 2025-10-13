def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  type = get_drink_type()
  print(size, type)

def get_size():
  res = input("What size drink would you like? \n[a] small \n[b] medium \n[c] large \n")
  if(res == 'a'):
    res = 'Small'
  elif(res == 'b'):
    res = 'Medium'
  elif(res == 'c'):
    res = 'Large'
  else:
    print_message()
    get_size()
  return res.lower()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n')
  if(res == 'a'):
    res = 'Brewed Coffee'
  elif(res == 'b'):
    res = 'Mocha'
  elif(res == 'c'):
    res = 'Latte'
  else:
    print_message()
    get_size()
  return res.lower()
  return res.lower()
  
coffee_bot()