def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  print(size)

def get_size():
  res = input("What size drink would you like? \n[a] small \n[b] medium \n[c] large \n")
  return res

coffee_bot()