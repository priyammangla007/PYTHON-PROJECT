

# Number Guessing Game

## Overview

This is a simple, interactive Python console game where the player tries to guess a randomly generated secret number within a limited number of attempts. The game provides feedback after each guess, indicating whether the guess is too high or too low. At the end, it analyzes the player's guesses and estimates their probability of winning as well as how many additional tries they would have needed if they guessed optimally.

## Features

- Random number generation within a defined range (default 1-100)
- Limited number of attempts per game (default 7 tries)
- Input validation with error handling (non-integer input, out-of-range guesses, repeated guesses)
- Feedback hints to guide the player to guess higher or lower
- Probability calculation based on guesses to estimate winning chances
- Analysis of minimum additional tries needed based on current guesses assuming optimal binary search strategy
- User-friendly console interface with welcome messages and clear instructions


## Technologies/Tools Used

- Python 3 (standard library only)
- Built-in modules:
    - `random` for generating the secret number
    - `sys` for exit handling
    - `time` for adding delay in messages to improve user experience


## Installation \& Running the Project

1. Ensure Python 3 is installed on your system. You can download it from https://www.python.org/downloads/
2. Download or clone the project files to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the game script with:

```
python number_guessing_game.py
```

5. Follow the on-screen instructions to play.

## Testing Instructions

- Run the program and try guessing numbers within and outside the specified range.
- Enter invalid inputs like letters or special characters to confirm input validation works.
- Attempt repeated guesses to verify the program prompts you accordingly.
- Play multiple games to see how the probability and additional tries estimation changes based on your guesses.
- Observe the final analysis once the game ends to understand your performance.



***

