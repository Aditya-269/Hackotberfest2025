import random

# List of words
words = ["python", "developer", "hangman", "programming", "computer", "keyboard"]

# Choose a random word
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
attempts = 6
guessed_letters = []

print("=== 🎮 Welcome to Hangman Game ===")

while attempts > 0 and "_" in guessed_word:
    print("\nWord: " + " ".join(guessed_word))
    print(f"Attempts remaining: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess.")
        attempts -= 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game Over! The word was:", word_to_guess)
