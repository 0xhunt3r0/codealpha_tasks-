import random



# Step 1: Predefined list of words
words = ["book", "car", "house", "tree", "ocean"]

# Step 2: Choose a random word
word = random.choice(words)
guessed_letters = []
trynb = 6

print("Welcome to Hangman game:")
print("Guess a word of this list :{book , car , house , tree , ocean }.")
print(f"You have {trynb} incorrect guesses allowed.\n")

# Step 3: Main game loop
while trynb > 0:
    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())

    # Check if player has guessed all letters
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Ask player for a letter
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Good guess!\n")
    else:
        trynb -= 1
        print(f"❌ Wrong! You have {trynb} trynb left.\n")

# Step 4: Game over
if trynb == 0:
    print("💀 Game Over! The word was:", word)
