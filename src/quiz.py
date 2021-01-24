import random
import time

lives = 3
score = 0
difficulty = 0
t = 3
clue = 3

dashes = ("\n---------------------------------------------------")

categories = {
  "CONTINENT" : ["EUROPE", "ASIA", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "ANTARTICA", "OCEANIA"],
  "COLOUR" : ["RED", "BLUE", "GREEN", "PINK", "PURPLE"],
  "SPORTS" : ["TENNIS", "BASKETBALL", "FOOTBALL", "VOLLEYBALL", "HOCKEY"],
  "UK CITY": ["LONDON", "BIRMINGHAM", "MANCHESTER", "LIVERPOOL", "YORK"],
  "CODING LANGUAGES": ["PYTHON", "JAVASCRIPT", "JAVA", "TYPESCRIPT", "RUBY", "C"]
  }

# This function removes the correct answer from the dictionary
def remove_answer():
  global answer # global keyword allows you to modify/use the variable outside of the current scope
  val_to_del = answer
  for key in categories[user_input]: 
    if val_to_del in categories[user_input]:
      categories[user_input].remove(val_to_del)
  print(len(categories[user_input]), " rounds remaining.")

# This function counts down time from 3 seconds and then clears the jumble word
def countdown(t): 
  while t != -1:
    mins, secs = divmod(t, 60) # the divmod function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(*jumble," ", timer, sep='', end="\r") 
    #the * brings it out of the list, then sep removes the spaces/commas
    time.sleep(1) 
    t -= 1

# This function increases score if the question is answered correctly
def score_increase():
  global score
  score += 1
  print("Your score is: ", score)
  
# This function randomly selects a word from the chosen category and jumbles it
def random_selection():
  selection = random.choice(categories[user_input])
  global answer
  answer = selection
  global jumble
  jumble = list(selection)
  random.shuffle(jumble)

# This function asks you if you want a clue and gives you a clue
def clue_func():
  global clue_choice
  clue_choice = input("Wrong answer!!! \nWould you like a Clue, yes/no: ").lower()
  if clue_choice == "yes" or clue_choice == "y":
    global answer
    print(f"The first letter of the word is {answer[0]}")

# This function asks user to guess again if answer is wrong
def new_guess():
  new_guess = input("Guess again: ").upper()
  while new_guess != answer:
    life_wrong()
    global clue_choice
    if clue_choice == "yes" or clue_choice == "y":
      new_guess = input(f"Even with a clue, LOL...guess again: ").upper()
    else:
      new_guess = input(f"Guess again: ").upper()
  print("\n")

# This function removes a life if you get an answer wrong
def life_wrong():
  global lives
  lives -= 1
  print(f"You got this wrong! You have {lives} lives remaining")
  if lives == 0:
    print("\n No juice left in the tank \n\n!!!!!!GAME OVER!!!!!!")
    time.sleep(1)
    print(f"Your final score is {score} and you had {lives} lives remaining.\n\n\n")
    # print(end_game)
    exit()


#This function asks the player to select a category
def choose_category():
  print("\nSelect a category out of:")
  for key in categories:
    print(key.title())
  print(dashes)
  global user_input
  user_input = input("Category Choice: ").upper()
  while user_input not in categories:
    user_input = input("Select from list above: ").upper()
  

#################################Live Code##########################################

print (
  """             
  Welcome to the Academy Anagram Game!
  👋 """)

print (
  """ 
  HOW TO COMPLETE THE GAME:
  - Choose a category.
  - Unscramble the jumbled word and type out your guess.
  - If you get it wrong, not to worry, you can get a clue!
  - Guess all the words from each category!
  - However, be careful not to get too many wrong! 
  - NOTE: YOU ONLY HAVE 3 LIVES!👀
  \n
  INCREASED DIFFICULTY:
  - Difficulty increases when you transition to the next category
  - You have 3 seconds to look at the jumbled word
  - Then it will disappear and you will then be able to guess
""")

      
while len(categories) > 0 and lives > 0:
  choose_category()
  while len(categories[user_input]) > 0 and lives > 0:
    random_selection()
    print (dashes)
    print("What " + user_input.title() + " is this?")
  
    if difficulty >= 1:
      countdown(t)
      print("*******POOOOF*******")
    else:
      print (*jumble, sep='') 
      #the * brings it out of the list, then sep removes the spaces/commas
    guess = input("Answer: ")
    guess = guess.upper()

    if guess == answer:
      print ("Got It!")
      #then remove this answer from the list
      time.sleep(0.5)
      remove_answer() 
      score_increase()
      time.sleep(0.5)
    else:
      life_wrong()
      clue_func()
      new_guess()
      remove_answer()
      score_increase()

  del categories[user_input]
  difficulty += 1

print("\nCONGRATULATIONS, you've reached the end of the game!")

print(f"Your final score is {score} and you had {lives} lives remaining.\n\n\n")
