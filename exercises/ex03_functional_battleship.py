"""EX03 - Functional Battleship !!!"""
 
__author__ = "730470758"

import random


def input_guess(grid_size: int, row_col: str) -> int:
    """Input Guess."""
    if row_col == "row":
        guess_row: str = input("Guess a row: ")
        guess_row_int: int = int(guess_row)
        while guess_row_int > grid_size or guess_row_int <= 0:
            guess_row = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
            guess_row_int = int(guess_row)
        return guess_row_int
    if row_col == "column":
        guess_column: str = input("Guess a column: ")
        guess_column_int = int(guess_column)
        while guess_column_int > grid_size or guess_column_int <= 0:
            guess_column = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
            guess_column_int = int(guess_column)
        return guess_column_int
    assert row_col == "row" or row_col == "column"
    return grid_size


def print_grid(grid_size: int, guess_row_int: int, guess_column_int: int, correct_guess: bool) -> None:
    """Print grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    result: str = RED_BOX
    row_counter: int = 1
    while row_counter <= grid_size:
        column_counter: int = 1
        row: str = ""
        if guess_row_int == row_counter:
            while column_counter <= grid_size:
                if guess_column_int == column_counter:
                    if correct_guess is False:
                        row += WHITE_BOX
                    else:
                        row += result
                else:
                    row += BLUE_BOX
                column_counter += 1
        else:
            row += BLUE_BOX * grid_size
        print(row)            
        row_counter += 1
    if correct_guess is True:
        print("Hit!")
    else:
        print("Miss!")


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Check correct guess."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main program."""
    counter: int = 1
    turn_counter: int = 1
    correct_counter: int = 0
    while counter <= 5:
        print(f"=== Turn {counter}/5 ===")
        guess_row_int: int = input_guess(grid_size, "row")
        guess_column_int: int = input_guess(grid_size, "column")
        Guess: bool = correct_guess(secret_row, secret_column, guess_row_int, guess_column_int)
        print_grid(grid_size, guess_row_int, guess_column_int, Guess)
        if Guess is False:
            turn_counter += 1
        else:
            print(f"You won in {turn_counter}/5 turns!")
            correct_counter += 1
            break
        counter += 1
    if correct_counter == 0:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
