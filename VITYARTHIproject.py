import random
import sys
import time


def get_valid_guess(lower, upper, previous_guesses):
    while True:
        try:
            guess = input(f"Enter your guess ({lower}-{upper}): ")
            guess = int(guess)
            if guess in previous_guesses:
                print(f"You already guessed {guess}. Try a different number.")
                time.sleep(1)
                continue
            if guess < lower or guess > upper:
                print(f"Please enter a number between {lower} and {upper}.")
                time.sleep(1)
                continue
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            time.sleep(1)


def analyze_guesses(guesses, secret, lower, upper):
    possible = set(range(lower, upper + 1))
    for g in guesses:
        if g < secret:
            possible = set(x for x in possible if x > g)
        elif g > secret:
            possible = set(x for x in possible if x < g)
    remaining = len(possible)
    total = upper - lower + 1
    prob = 1 - remaining / total
    return max(0, min(1, prob))


def min_additional_tries(guesses, secret, lower, upper):
    # Calculate how many more tries would be needed assuming an optimal binary search on the reduced range
    possible = set(range(lower, upper + 1))
    for g in guesses:
        if g < secret:
            possible = set(x for x in possible if x > g)
        elif g > secret:
            possible = set(x for x in possible if x < g)
    remaining = len(possible)
    # Number of tries in worst-case binary search = ceil(log2(remaining))
    import math
    if remaining <= 1:
        return 0
    return math.ceil(math.log2(remaining))


def number_guessing_game():
    lower = 1
    upper = 100
    max_attempts = 7
    secret = random.randint(lower, upper)
    guesses = []

    print(f"Welcome to the Number Guessing Game!")
    time.sleep(1)
    print(f"Guess the number between {lower} and {upper}. You have {max_attempts} tries.")

    for attempt in range(1, max_attempts + 1):
        guess = get_valid_guess(lower, upper, guesses)
        guesses.append(guess)

        if guess < secret:
            print("Try a higher number.")
        elif guess > secret:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret} in {attempt} tries.")
            sys.exit(0)
        time.sleep(1)
    else:
        print(f"Sorry, you've used all your tries. The number was {secret}. Try again!")

    probability = analyze_guesses(guesses, secret, lower, upper)
    print(f"Based on your answers, your probability of winning was approximately {probability:.2%}.")

    more_tries_needed = min_additional_tries(guesses, secret, lower, upper)
    print(f"Based on your guesses so far, "
          f"you could have found the secret number in about {more_tries_needed} more "
          f"optimally chosen guess{'es' if more_tries_needed != 1 else ''}.")


if __name__ == "__main__":
    number_guessing_game()
