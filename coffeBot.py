def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  type = get_drink_type()
  print(size, type)

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input("What size drink would you like? \n[a] small \n[b] medium \n[c] large \n")
  res = res.lower()
  if(res == 'a'):
    res = 'Small'
  elif(res == 'b'):
    res = 'Medium'
  elif(res == 'c'):
    res = 'Large'
  else:
    print_message()
    get_size()
  return res

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n')
  res = res.lower
  if(res == 'a'):
    res = 'Brewed Coffee'
  elif(res == 'b'):
    res = 'Mocha'
  elif(res == 'c'):
    res = 'Latte'
  else:
    print_message()
    get_size()
  return res

def get_milk_type():
  res = input('What kind of milk would you like with that? \n[a] Full Fat \n[b] Semi Skimmed \n[c] Plant Based')
  res = res.lower()
  if(res == 'a'):
    res = 'Full Fat'
  elif(res == 'b'):
    res = 'Semi Skimmed'
  elif(res == 'c'):
    res = 'Plant Based'
  else:
    print_message()
    get_size()
  return res

  
coffee_bot()