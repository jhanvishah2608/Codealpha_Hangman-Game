import random

word_list = ["mango", "python", "laptop", "school", "button"]

secret_word = random.choice(word_list)

blanks = []
for letter in secret_word:
    blanks.append("_")

wrong_guesses = 0
max_wrong = 6
guessed_letters = []

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")


while wrong_guesses < max_wrong:

    print("Word:", " ".join(blanks))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Letters guessed:", guessed_letters)

    if "_" not in blanks:
        print("\nYou WIN! The word was:", secret_word)
        break

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter! Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")

        i = 0
        for letter in secret_word:
            if letter == guess:
                blanks[i] = guess
            i = i + 1

    else:
        print("Wrong!")
        wrong_guesses = wrong_guesses + 1

if wrong_guesses == max_wrong:
    print("\nYou LOST! The word was:", secret_word)
