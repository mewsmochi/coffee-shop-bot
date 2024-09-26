# Define your functions
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
  if res == 'a' or res == 'A':
    return 'small'
  elif res == 'b' or res == 'B':
    return 'medium'
  elif res == 'c' or res == 'C':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a' or res == 'A':
    return 'brewed coffee'
  elif res == 'b' or res == 'B':
    return 'mocha'
  elif res == 'c' or res == 'C':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_drink_temp():
  res = input("Would you like your drink hot or iced? \n[a] Hot \n[b] Iced \n> ")
  if res == 'a' or res == 'A':
    return 'hot'
  elif res == 'b' or res == 'B':
    return 'iced'
  else:
    print_message()
    return get_drink_temp()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
  if res == 'a' or res == 'A':
    return 'latte'
  elif res == 'b' or res == 'B':
    return 'non-fat latte'
  elif res == 'c' or res == 'C':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def cup_type():
  res = input("Do you want a plastic cup, or do you have a reusable one? \n[a] Plastic \n[b] Reusable")
  if res == 'a' or res == 'A':
    print("No problem! We'll provide you a plastic cup.")
  elif res == 'b' or res == 'B':
    print("Very environmentally friendly! We'll fill that up for you.")
  else:
    print_message()
    return cup_type()

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  drink_temp = get_drink_temp()
  print('Alright, that\'s a ' + size + " " + drink_temp + " " + drink_type + "!")
  cup_type()
  name = input("May I have your name please? \n> ")
  print("Thanks, " + name + "! Your drink will be ready shortly.")

# Call coffee_bot()!
coffee_bot()
