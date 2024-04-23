"""EX02 - One Shot Battleship !!!"""
 
__author__ = "730470758"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: str = input("Guess a row: ")
guess_row_int: int = int(guess_row)
while guess_row_int > grid_size or guess_row_int < 0:
    guess_row = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    guess_row_int = int(guess_row)
guess_column: str = input("Guess a column: ")
guess_column_int = int(guess_column)
while guess_column_int > grid_size or guess_column_int < 0:
    guess_column = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    guess_column_int = int(guess_column)

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
                if guess_column_int != secret_column or guess_row_int != secret_row:
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
if guess_row_int == secret_row and guess_column_int == secret_column:
    print("Hit!")
elif guess_row_int == secret_row and guess_column_int != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_row_int != secret_row and guess_column_int == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!") 