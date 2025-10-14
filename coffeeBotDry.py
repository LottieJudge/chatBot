def user_choice(options, prompt):
  while True:
    res = input(prompt).lower()
    if res in options:
      return options[res]
    else:
      print_message()

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  type = get_drink_type()
  print(F"Alright that's a {size} {type}! Coming right up kid")
  name = input("Woah woah woah bub, got a name? ")
  print(f"alright, wait over there {name}, your drink will be with you in uno momento, capish?")

def print_message():
  print("Didn't quite catch that pal, come again?")

def get_size():
  options = {
    'a': 'small',
    'b': 'medium', 
    'c': 'large'
  }
  prompt = "What size? \n[a] Small \n[b] Medium \n[c] Large \n"
  return user_choice(options, prompt)

def get_drink_type():
  options = {
    'a': 'Brewed Coffee',
    'b': 'Mocha',
    'c': 'Latte'
  }
  prompt = "and what drink is that gonna be bub? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n"
  drink_type = user_choice(options, prompt)
  if drink_type == 'Latte':
      return order_latte()
  return drink_type

def order_latte():
  options = {
    'a': 'Full Fat Latte',
    'b': 'Semi Skimmed Latte',
    'c': 'Plant Based Latte'
  }
  prompt = "what kind of milk would you like with hat? \n[a] Full Fat \n[b] Semi Skimmed \n[c] Plant Based \n"
  return user_choice(options, prompt)

coffee_bot()