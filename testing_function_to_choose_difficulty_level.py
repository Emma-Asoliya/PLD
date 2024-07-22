import random
import os
import time

# List of symbols for the cards
symbols = ['🤎', '🤩', '🤑', '🤡', '😎', '😂', '😏', '🥵']
medium_symbols = symbols + ['🤠', '😇', '😜', '🧐', '🤯', '🥳']
hard_symbols = medium_symbols + ['🤬', '🤢', '🤧', '🤓', '🤠', '😇', '😜', '🧐']

# Shuffle the symbols for each difficulty level
def shuffle_symbols(symbols):
    symbols = symbols * 2  # To make pairs
    random.shuffle(symbols)
    return symbols

# Function to print the board
def print_board(board, revealed):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('❓ ', end=' ')
        print()

# Function to get the player's card selection
def get_card_selection(board, revealed):
    size = len(board)
    row1 = int(input(f'Enter the row for the first card (0-{size-1}): '))
    col1 = int(input(f'Enter the column for the first card (0-{size-1}): '))
    revealed[row1][col1] = True

    os.system('clear')  # Use 'cls' if you're on Windows
    print_board(board, revealed)

    row2 = int(input(f'Enter the row for the second card (0-{size-1}): '))
    col2 = int(input(f'Enter the column for the second card (0-{size-1}): '))
    revealed[row2][col2] = True

    os.system('clear')  # Use 'cls' if you're on Windows
    print_board(board, revealed)

    if board[row1][col1] != board[row2][col2]:
        print('No match! Try again.')
        time.sleep(2)  # Pause to let the user see the result
        revealed[row1][col1] = False
        revealed[row2][col2] = False
    else:
        print('Match found!')

# Function to display the difficulty levels
def select_difficulty():
    while True:
        os.system('clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                            ✨ Select Difficulty Level ✨                             ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1. Easy (4x4 grid)")
        print("2. Medium (6x6 grid)")
        print("3. Hard (8x8 grid)")
        print("4. Back to Menu")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            return 4
        elif choice == '2':
            return 6
        elif choice == '3':
            return 8
        elif choice == '4':
            return None
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            time.sleep(2)

# Function to display instructions
def display_instructions():
    os.system('clear')
    print("📜 Memory Game Instructions:")
    print("1. The game board contains pairs of hidden symbols.")
    print("2. On each turn, you can reveal two cards.")
    print("3. If the symbols on the cards match, they remain revealed.")
    print("4. If they do not match, they will be hidden again.")
    print("5. The game continues until all pairs are matched.")
    print("Goodluck 🤞") 
    print("\nPress Enter to return to the menu.")
    input()  # Waits for the user to press Enter so that they can go back to the menu

# Function to display about
def display_about():
    os.system('clear')
    print("📜 About Memory Game:")
    print("Version: 1.0")
    print("Author: NegPod 9")
    print("This game is a simple memory matching game developed as a project that aims to support cognitive health for all in Africa and beyond.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter

# Function to set up the game board based on difficulty level
def setup_board(difficulty):
    if difficulty == '1':  # Easy
        size = 4
        symbols = shuffle_symbols(['🤎', '🤩', '🤑', '🤡', '😎', '😂', '😏', '🥵'])
    elif difficulty == '2':  # Medium
        size = 6
        symbols = shuffle_symbols(medium_symbols)
    elif difficulty == '3':  # Hard
        size = 8
        symbols = shuffle_symbols(hard_symbols)
    
    board = [[symbols.pop() for _ in range(size)] for _ in range(size)]
    revealed = [[False] * size for _ in range(size)]
    return board, revealed

# Function to choose difficulty level
def choose_difficulty():
    while True:
        os.system('clear')
        print("Choose Difficulty Level:")
        print("1. Easy (4x4 grid)")
        print("2. Medium (6x6 grid)")
        print("3. Hard (8x8 grid)")
        
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            time.sleep(2)

# Main game loop
def start_game():
    difficulty = choose_difficulty()
    board, revealed = setup_board(difficulty)
    os.system('clear')
    print_board(board, revealed)

    while not all(all(row) for row in revealed):
        get_card_selection(board, revealed)
    
    print("Congratulations! All matching pairs have been found.")
