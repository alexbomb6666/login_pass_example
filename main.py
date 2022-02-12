from replit import db
from googletrans import Translator, constants
from pprint import pprint
def register():
  global user, password
  print("Mk, what is the username?")
  user = input()
  print("Password?")
  password = input()
  try:
    value = db[user + "_password"]
    
  except KeyError:
    db[user] = user
    db[user + "_password"] = password
    print("Your profile is registered. Login now.")
    print(f"Your login is {user} and password is {password}. Write that on a paper!")
    exit()
  print("R u kidding me? You already have the profile! Use login next time.")
  exit()


def login():
  global user, password
  print("Username?")
  user = input()
  print("Password")
  password = input()
  try:
    value = db[user + "_password"]
  except KeyError:
    print("Incorrect details! (this account does not exist)")
    return
  if db[user + "_password"] == password:
    print("You got passed through! Have fun using!")
    return True
  else:
    print("Incorrect details!")
    return False


def main_page():
  print("Welcome! We have features like: \n 1. Weather \n 2. Translator \n 3. Delete account")
  print("To use the feature, just type the name of it! Weather/Translator/Delete account")
  main_choose(input())


def main_choose(chosen):
  if chosen == "Translator":
    flag = False
    while flag is False:
      translator = Translator()
      print("What do you want to translate?")
      word = input()
      print("On what origin? Type something like an example: ru/eu/fr/en \n \n type en if you want to translator to something else \n or type none if you want to go back to main page")
      origin = input()
      if origin != "none":
        translation = translator.translate(word, dest=origin)
        print(f"Your translation is {translation.text}!")
      else:
        flag = True
    return
    main_page()
print("Hello, its Alexbomb service!")
print("Do you want to login or register? Type login/register")
login_reg = input()
if login_reg == "register":
  register()
  
elif login_reg == "login":
  if_pass = login()
  if if_pass is True:
    main_page()
  else:
    exit()
else:
  print("Sorry, didnt understand what did you say! Say register or login next time!")
  exit