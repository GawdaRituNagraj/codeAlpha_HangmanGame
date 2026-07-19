import random
# ── Word list ──────────────────────────────────────────────────────────────────
WORDS = ["python", "hangman", "codealpha", "program", "internship"]
# ── Game logic ─────────────────────────────────────────────────────────────────
def play_hangman():
    secret_word = random.choice(WORDS)          # pick a random word
    guessed_letters = []                         # letters the player has tried
    wrong_guesses = 0                            # count of wrong attempts
    max_wrong = 6                                # limit incorrect guesses to 6
    print("\n=============================")
    print("   Welcome to HANGMAN! ")
    print("=============================")
    print(f"The word has {len(secret_word)} letters.")
    print(f"You have {max_wrong} incorrect guesses allowed.\n")
    # ── Main game loop ─────────────────────────────────────────────────────────
    while wrong_guesses < max_wrong:
        # Build the display: show guessed letters, underscore for unknowns
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print(f"Word:  {display}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Letters tried: {', '.join(sorted(guessed_letters)) or 'none'}")
        # Check win condition before asking for input
        if "_" not in display:
            print(f"\n You won! The word was '{secret_word}'.")
            return
        # ── Get player input ───────────────────────────────────────────────────
        guess = input("\nGuess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print(f" You already tried '{guess}'. Pick a different letter.\n")
            continue
        guessed_letters.append(guess)           # record the guess
        # ── Check if the guess is correct ──────────────────────────────────────
        if guess in secret_word:
            print(f" '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            remaining = max_wrong - wrong_guesses
            print(f" '{guess}' is NOT in the word. "
                  f"{remaining} wrong guess(es) left.\n")
    # ── Player ran out of guesses ──────────────────────────────────────────────
    print(f" Game over! You ran out of guesses.")
    print(f"The word was '{secret_word}'.\n")
# ── Play again loop ────────────────────────────────────────────────────────────
def main():
    while True:
        play_hangman()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye. \n")
            break
if __name__ == "__main__":
    main()

