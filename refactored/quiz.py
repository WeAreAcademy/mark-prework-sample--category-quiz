import random
import time

lives = 3
score = 0
t = 3

dashes = ("\n---------------------------------------------------")

categories = {
  "CONTINENT" : ["EUROPE", "ASIA", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "ANTARTICA", "OCEANIA"],
  "COLOUR" : ["RED", "BLUE", "GREEN", "PINK", "PURPLE"],
  "SPORTS" : ["TENNIS", "BASKETBALL", "FOOTBALL", "VOLLEYBALL", "HOCKEY"],
  "UK CITY": ["LONDON", "BIRMINGHAM", "MANCHESTER", "LIVERPOOL", "YORK"],
  "CODING LANGUAGES": ["PYTHON", "JAVASCRIPT", "JAVA", "TYPESCRIPT", "RUBY", "C"]
  }

# This function removes the correct answer from the categories dictionary
def remove_answer(category, word_to_guess):
  categories[category].remove(word_to_guess)
  print(len(categories[category]), " rounds remaining.")

# This function counts down time from 3 seconds and then clears the jumble word
def countdown(t, jumbled_word): 
  while t != -1:
    mins, secs = divmod(t, 60) # the divmod function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(*jumbled_word," ", timer, sep='', end="\r") 
    #the * brings it out of the list, then sep removes the spaces/commas
    time.sleep(1) 
    t -= 1

# Increases score and prints new score
def score_increase():
  global score
  score += 1
  print("Your score is: ", score)

# Randomly chooses a word from the chosen category
def get_word(category):
  return random.choice(categories[category])

# Shuffles the letters in a word
def jumble_word(word):
  to_jumble = list(word)
  random.shuffle(to_jumble)
  return to_jumble

# Asks you if you want a clue and gives you a clue if so
def give_clue(word_to_guess):
  clue_input = input("Wrong answer!!! \nWould you like a Clue, yes/no: ").lower()
  wants_clue = (clue_input == "yes" or clue_input == "y")
  if wants_clue:
    print(f"The first letter of the word is {word_to_guess[0]}")
  return wants_clue

# Asks user to guess again
def get_later_guess(word_to_guess, wants_clue):
  new_guess = input("Guess again: ").upper()
  while new_guess != word_to_guess:
    lose_life()
    if wants_clue:
      new_guess = input(f"Even with a clue, LOL...guess again: ").upper()
    else:
      new_guess = input(f"Guess again: ").upper()
  return new_guess

# Removes a life and checks if ran out of lives
def lose_life():
  global lives
  lives -= 1
  # TODO: make the word life dynamic - eg 1 life, 2 lives ...
  print(f"You got this wrong! You have {lives} lives remaining")
  if lives == 0:
    print("\n No juice left in the tank \n\n!!!!!!GAME OVER!!!!!!")
    time.sleep(1)
    print(f"Your final score is {score}.\n\n\n")
    exit()


# Asks user to pick category
def choose_category():
  print("\nSelect a category out of:")
  for key in categories:
    print(key.title())
  print(dashes)
  user_input = input("Category Choice: ").upper()
  while user_input not in categories:
    user_input = input("Select from list above: ").upper()
  return user_input

# Prints welcome and instructions
def print_welcome():
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

# Prints jumbled word (and hides it if difficulty higher)
def give_starting_point(difficulty, jumbled_word):
  if difficulty >= 1:
      countdown(t, jumbled_word)
      print("*******POOOOF*******")
  else:
      print (*jumbled_word, sep='') 
      #the * brings it out of the list, then sep removes the spaces/commas

# Calls other functions to hadnle correct answer
def handle_right_answer(category, word_to_guess):
  print ("Got It!")
  time.sleep(0.5)
  remove_answer(category, word_to_guess) 
  score_increase()
  time.sleep(0.5)

# Checks if guess is correct and calls functions for each option
def handle_guess(guess, word_to_guess, category):
  if guess == word_to_guess:
      handle_right_answer(category,word_to_guess)
  else:
      lose_life()
      wants_clue = give_clue(word_to_guess)
      next_guess = get_later_guess(word_to_guess, wants_clue)
      if next_guess == word_to_guess:
        handle_right_answer(category, word_to_guess)

# Governs the play of a single category
def play_category(category, difficulty):
  while len(categories[category]) > 0 and lives > 0:
      word_to_guess = get_word(category)
      jumbled_word = jumble_word(word_to_guess)
      print (dashes)
      print("What " + category.title() + " is this?")
      give_starting_point(difficulty,jumbled_word)
      guess = input("Your guess: ").upper()
      handle_guess(guess, word_to_guess, category)
  
# Overall game
def play_game():
  difficulty = 0
  print_welcome()

  while len(categories) > 0 and lives > 0:
    category = choose_category()
    play_category(category, difficulty)

    del categories[category]
    difficulty += 1

  print("\nCONGRATULATIONS, you've reached the end of the game!")
  print(f"Your final score is {score} and you had {lives} lives remaining.\n\n\n")

# Executes the main game function
play_game()