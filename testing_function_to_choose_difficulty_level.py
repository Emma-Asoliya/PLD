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


# Main game loop
def start_game():
    size = select_difficulty()
    if size is None:
        return

    board = initialize_board(size)
    revealed = [[False] * size for _ in range(size)]
    
    while True:
        os.system('clear')
        print_board(board, revealed)
        get_card_selection(board, revealed)
        # Add your win condition check and other game logic here

# Main menu function
def display_menu():
    while True:
        os.system('clear')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                            ✨ Welcome to the Memory Game ✨                             ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1. Start Game")
        print("2. Instructions")
        print("3. About")
        print("4. View Leaderboard")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            start_game()
        elif choice == '2':
            display_instructions()
        elif choice == '3':
            display_about()
        elif choice == '4':
            display_leaderboard()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            time.sleep(2)

display_menu()
