# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

import sys  # Import the sys module

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# Choose a random word from the dictionary
# hidden_word = random.choice(FIVE_LETTER_WORDS)
hidden_word = "agile"
def wordle():
    game_ended = False

    def enter_action(input):
        nonlocal gw, game_ended
        input = input.lower()
        score = 0

        if game_ended:
            return

        # Check if the entered string is a legitimate English word
        if input.lower() in FIVE_LETTER_WORDS:
            # gw.show_message("Great! You guessed a legitimate English word.")
            score = 0
            # Get the current row from WordleGWindow
            current_row = gw.get_current_row()

            # Compare each letter in the guess with the hidden word
            for index, input_char in enumerate(input):
                # Get the corresponding letter in the hidden word
                hidden_letter = hidden_word[index]

                # Determine the color based on the comparison
                if input_char == hidden_letter and hidden_word[index] == input_char:
                    score += 1
                    color = CORRECT_COLOR
                elif input_char in hidden_word:
                    color = PRESENT_COLOR
                else:
                    color = MISSING_COLOR

                # Set the color for the square
                gw.set_square_color(current_row, index, color)

            if score == N_COLS or current_row == N_ROWS - 1:
                if score == N_COLS:
                    gw.show_message("Congrats! You completed Wordle in {} tries.".format(current_row + 1))
                else:
                    gw.show_message("The answer was " + hidden_word + ". Thanks for trying!")

                game_ended = True  # Set the game as ended
            

            # Increment the current row for the next guess
            gw.set_current_row(current_row + 1)

        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Wait for the user to close the window before exiting
    gw.wait_for_close()

# Startup code
if __name__ == "__main__":
    wordle()
