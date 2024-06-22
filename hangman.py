import random

# Hangman graphics for different stages
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===
    ''', '''
     +---+
     O   |
         |
         |
        ===
    ''', '''
     +---+
     O   |
     |   |
         |
        ===
    ''', '''
     +---+
     O   |
    /|   |
         |
        ===
    ''', '''
     +---+
     O   |
    /|\\  |
         |
        ===
    ''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===
    ''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    '''
]

# Words for different categories
WORDS = {
    "animals": ["elephant", "giraffe", "kangaroo", "dolphin", "cheetah"],
    "countries": ["australia", "brazil", "canada", "denmark", "egypt"],
    "movies": ["inception", "gladiator", "titanic", "avatar", "rocky"]
}

# Difficulty levels
DIFFICULTY_LEVELS = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

def choose_category():
    print("Choose a category:")
    for category in WORDS.keys():
        print(category.capitalize())
    while True:
        category = input("Enter your choice: ").lower()
        if category in WORDS:
            return category
        else:
            print("Invalid category. Please try again.")

def choose_difficulty():
    print("Choose a difficulty level (easy, medium, hard):")
    while True:
        difficulty = input("Enter your choice: ").lower()
        if difficulty in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[difficulty]
        else:
            print("Invalid difficulty level. Please try again.")

def get_word(category):
    return random.choice(WORDS[category])

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print("Missed letters:", ' '.join(missed_letters))
    
    blanks = '_' * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    print(' '.join(blanks))
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    return input("Do you want to play again? (yes or no) ").lower().startswith('y')

def show_hint(secret_word, correct_letters):
    for letter in secret_word:
        if letter not in correct_letters:
            print(f"Hint: One of the letters is '{letter}'")
            break

def hangman():
    print("H A N G M A N")
    category = choose_category()
    difficulty = choose_difficulty()
    
    missed_letters = ''
    correct_letters = ''
    secret_word = get_word(category)
    game_is_done = False
    hints_used = 0
    max_hints = 2

    while True:
        display_board(missed_letters, correct_letters, secret_word)
        
        if hints_used < max_hints:
            hint_prompt = input("Do you want a hint? It will reduce your overall score. (yes or no) ").lower()
            if hint_prompt.startswith('y'):
                show_hint(secret_word, correct_letters)
                hints_used += 1
        
        guess = get_guess(missed_letters + correct_letters)
        
        if guess in secret_word:
            correct_letters += guess
            
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"Yes! The secret word is '{secret_word}'! You have won!")
                game_is_done = True
        else:
            missed_letters += guess
            
            if len(missed_letters) == difficulty:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was '{secret_word}'")
                game_is_done = True
        
        if game_is_done:
            if play_again():
                category = choose_category()
                difficulty = choose_difficulty()
                missed_letters = ''
                correct_letters = ''
                game_is_done = False
                secret_word = get_word(category)
                hints_used = 0
            else:
                break

# Start the game
hangman()