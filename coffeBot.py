def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  type = get_drink_type()
  print(F"Alright that's a {size} {type}! Coming right up kid")
  name = input("Woah woah woah bub, got a name? ")
  print(f"alright, wait over there {name}, your drink will be with you in uno momento, capish?")

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
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  res = res.lower()
  if(res == 'a'):
    res = 'Brewed Coffee'
  elif(res == 'b'):
    res = 'Mocha'
  elif(res == 'c'):
    res = order_latte()
  else:
    print_message()
    get_drink_type()
  return res

def order_latte():
  res = input('What kind of milk would you like with that? \n[a] Full Fat \n[b] Semi Skimmed \n[c] Plant Based \n')
  res = res.lower()
  if(res == 'a'):
    res = 'Full Fat latte'
  elif(res == 'b'):
    res = 'Semi Skimmed Latte'
  elif(res == 'c'):
    res = 'Plant Based Latte'
  else:
    print_message()
    order_latte()
  return res

  
coffee_bot()