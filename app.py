import random

# List of words
words = ["python", "hangman", "computer", "programming", "science"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while tries > 0:
    # Show the word with underscores
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_ "
    print("\nWord:", display)

    # Check if word is guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("🏆 Congratulations! You guessed the word:", secret_word)
        break

    # Ask for player guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guess
    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        tries -= 1
        print("❌ Wrong! Tries left:", tries)

if tries == 0:
    print("\n💀 Game Over! The word was:", secret_word)
