"""A computer number-guessing game."""

from random import randint

best_score = None
attempt_limit = 12
computer_mode = False

print("Hello, what's your player name?")
name = input("(Type in your name) ")

print(f"Hi, {name}! Would you like to have the computer guess your number?")
user_mode_choice = input("[y]es or [n]o: ").upper()

if user_mode_choice == "Y" or user_mode_choice == "YES":
    computer_mode = True

if not computer_mode:
    while True:
        # Set the range of numbers for the game
        range_min = 1
        range_max = 100

        # Ask user for range_min and range_max
        should_get_range = input(
            "Would you like to set a custom range? "
        ).upper()

        if should_get_range == "Y" or should_get_range == "YES":
            while True:
                try:
                    range_min = int(input("Start range at: "))

                except ValueError:
                    print("That's not a number, try again")
                    continue

                break

            while True:
                try:
                    user_max = int(input("End range at: "))

                except ValueError:
                    print("That's not a number, try again")
                    continue

                # Check if user_max is larger than range_min
                if user_max <= range_min:
                    print(f"Please enter a number larger than {range_min}")
                    continue

                range_max = user_max
                break

        number = randint(range_min, range_max)
        guesses = 0

        print(
            f"{name}, I'm thinking of a number between {range_min}",
            f"and {range_max}.",
        )
        print("Can you guess what the number is?")

        while True:
            # Before allowing user to guess, check if they're within the limit
            if guesses > attempt_limit:
                print("Oh no! You've made too many guesses.")
                print("Computer victory. GAME OVER.")
                break

            # Validate input
            try:
                guess = int(input("Your guess? "))

            except ValueError:
                print("That's not an integer, try again")
                continue

            if guess < 1 or guess > 100:
                print("That's not between 1 and 100. Try again.")
                continue

            # User guessed a valid number; check if they're within the limit
            if guesses < attempt_limit:
                guesses += 1
            else:
                print(f"Sorry, you exceeded the max # of guesses.")
                print("Game Over :(")

            if guess < number:
                print("Your guess is too low, try again.")

            elif guess > number:
                print("Your guess is too high, try again.")

            else:
                print(f"Good job, {name}!")
                print(f"You found my number in {guesses} guesses!")
                break

        if best_score is None or guesses < best_score:
            best_score = guesses

        answer = input("Do you want to play again? ").upper()

        if answer != "Y" and answer != "YES":
            break

    print(f"Your best score was {best_score}.")

else:
    while True:
        # Set the range of numbers for the game
        range_min = 0
        range_max = 101

        computer_guess = None
        guesses = 0

        print("🤖 Think of a number between 1 and 100")
        print("🤖 I will guess your number now...")

        while True:
            computer_guess = (range_min + range_max) // 2
            guesses += 1
            print(f"🤖 Is the number {computer_guess}?")

            user_feedback = input(
                "Is the guess correct, too low, or too high? "
            ).upper()

            if user_feedback == "TOO LOW":
                range_min = computer_guess
                continue

            elif user_feedback == "TOO HIGH":
                range_max = computer_guess
                continue

            elif user_feedback == "CORRECT":
                print(f"🤖 I guessed your number in {guesses} guesses")
                print(f"🤖 Let's play again.")
                break

            else:
                print(f"🤖 I didn't understand that.")
                continue
