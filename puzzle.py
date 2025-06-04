secret_number = "elephant"

guess_count = 0

print("Welcome To Word Puzzle Game!")
print("\nYour hint is:_ _ _ _ _ _ _ _")

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if len(guess) != len(secret_number):
        print("\nPlease enter a word with", len(secret_number), "letters")
        continue

    if guess == secret_number:
        print(f"Congratulation! you guessed the word in {guess_count} guesses.")
    
        break
    hint = ""
    
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_number:
            hint += guess[i].lower()
        else:
            hint += "_"
    print("Hint:", hint)