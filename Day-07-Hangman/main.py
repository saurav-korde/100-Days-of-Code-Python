import random

# A list of hangman stages for visual representation
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# A list of words for the game
word_list = ["aardvark", "baboon", "camel", "galaxy", "python", "developer", "engineer"]

# --- Game Setup ---
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Create a list to represent the hidden word (e.g., ['_', '_', '_', '_', '_'])
display = []
for _ in range(word_length):
    display += "_"

print("Welcome to Hangman!")

# --- Main Game Loop ---
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed the letter '{guess}'.")

    # Check the guessed letter against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guess is wrong, the player loses a life
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The correct word was: {chosen_word}")

    # Join the list elements into a string for display
    print(f"{' '.join(display)}")

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current hangman stage
    print(stages[lives])