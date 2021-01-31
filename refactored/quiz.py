import random

dashes = ("\n---------------------------------------------------")


def remove_answer_from_category(answer, category):
    if answer in category:
        category.remove(answer)


# Randomly selects a word from the chosen category and jumbles its letters.
# Returns a tuple of two strings: (answer, jumbled answer)


def pick_random_question(category):
    answer = random.choice(category)
    remove_answer_from_category(answer, category)

    jumbled_letters = list(answer)
    random.shuffle(jumbled_letters)
    jumble = "".join(jumbled_letters)
    return answer, jumble


# Asks you if you want a clue and gives you a clue
# Returns True if you requested a clue, else False


def offer_and_give_clue(answer):
    clue_choice = input("Would you like a clue, yes/no: ").lower()
    if clue_choice == "yes" or clue_choice == "y":
        print(f"The first letter of the word is {answer[0]}")
        return True
    else:
        return False


# Asks the player to select a category
# Returns tuple: the chosen category name, its list of questions


def get_category_choice(categories):
    print("\nSelect a category out of:")
    for key in categories:
        print(key.title())
    print(dashes)
    category_name = input("Category Choice: ").upper()
    while category_name not in categories:
        category_name = input("Select from list above: ").upper()

    category = categories[category_name]
    del categories[category_name]

    return category, category_name


def display_intro():
    print("""
    Welcome to the Academy Anagram Game!
    👋 """)

    print(
        """
    HOW TO COMPLETE THE GAME:
    - Choose a category.
    - Unscramble the jumbled word and type out your guess.
    - If you get it wrong, not to worry, you can get a clue!
    - Guess all the words from each category!
    - However, be careful not to get too many wrong!
    - NOTE: YOU ONLY HAVE 3 LIVES!👀
    \n
    """)


def display_question(category_name, jumble):
    print(dashes)
    print(f"What {category_name.title()} is this?")
    print(jumble)

# Return the user's guess


def prompt_and_get_guess():
    return input("Guess: ").upper()


def say_wrong(has_used_clue, lives):
    if has_used_clue:
        print("Wrong!  Even with a clue, LOL...")
    else:
        print("Wrong!")
    print(f"Number of lives remaining: {lives}")


# Handle user guessing (and clue-giving) for the given question
# Returns number of lives remaining after guesses (possibly zero)


def handle_guesses(answer, lives):
    guessed_correctly = False
    has_used_clue = False

    while not guessed_correctly and lives > 0:
        guess = prompt_and_get_guess()
        if guess == answer:
            guessed_correctly = True
            print("Right!")
        else:
            lives -= 1
            say_wrong(has_used_clue, lives)
            if (lives > 0 and not has_used_clue):
                has_used_clue = offer_and_give_clue(answer)

    return lives


def create_categories():
    return {
        "CONTINENT": ["EUROPE", "ASIA", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "ANTARTICA", "OCEANIA"],
        "COLOUR": ["RED", "BLUE", "GREEN", "PINK", "PURPLE"],
        "SPORT": ["TENNIS", "BASKETBALL", "FOOTBALL", "VOLLEYBALL", "HOCKEY"],
        "UK CITY": ["LONDON", "BIRMINGHAM", "MANCHESTER", "LIVERPOOL", "YORK"],
        "CODING LANGUAGE": ["PYTHON", "JAVASCRIPT", "JAVA", "TYPESCRIPT", "RUBY", "C"]
    }


# Display an update of score and number of rounds remaining in the current category


def display_update(score, lives, category, category_name):
    print(f"Your score is: {score} and you have {lives} lives remaining.")
    rounds_remaining = len(category)
    if rounds_remaining > 0:
        print(f"{len(category)} rounds remain in the category {category_name}")
    else:
        print(f"That's the end of category {category_name}")


# Play one given category, asking questions from it until completed or no lives left.
# Returns a tuple of the updated counts of score and lives (possibly zero)


def play_category(category, category_name, lives, score):
    while len(category) > 0 and lives > 0:
        (answer, jumble) = pick_random_question(category)
        display_question(category_name, jumble)
        lives = handle_guesses(answer, lives)

        if lives > 0:
            score += 1
            display_update(score, lives, category, category_name)
    return lives, score


# Play the entire game


def play():
    lives = 3
    score = 0
    categories = create_categories()

    display_intro()

    while len(categories) > 0 and lives > 0:
        (category, category_name) = get_category_choice(categories)
        (lives, score) = play_category(category, category_name, lives, score)

    # At the end, either because lives exhausted or because all categories were completed.
    if (lives > 0):
        print("\nCONGRATULATIONS, you've reached the end of the game!")
    else:
        print("\nNo juice left in the tank\n\n!!!!!!GAME OVER!!!!!!")
    print(f"Your final score is {score} and you had {lives} lives remaining.\n\n\n")


play()
