#!/usr/bin/env python3
import random
import os
import time
import shutil

# List of symbols for the cards
symbols = ['🤎', '🤩', '🤑', '🤡', '😎', '😂', '😏', '🥵']
symbols = symbols * 2  # to make pairs

# To shuffle the symbols randomly
random.shuffle(symbols)

# Output the shuffled lists
print("Shuffled Symbols:", symbols)

# Function to print the board with larger "font"
def print_board(board, revealed):
    for i in range(4):
        for j in range(4):
            if revealed[i][j]:
                print(f" {board[i][j]} ", end='  ')  # Added spacing around emojis
            else:
                print(' ❓ ', end='  ')
        print("\n")  # Added a newline for better readability

# Function to get the player's card selection
def get_card_selection(board, revealed):
    while True:
        try:
            row1 = input('Enter the row for the first card (0-3) or q to return to the main menu: ')
            if row1.lower() == 'q':
                return False
            row1 = int(row1)
            col1 = int(input('Enter the column for the first card (0-3): '))
            if revealed[row1][col1]:
                print("Card already revealed. Choose another card.")
                continue
            revealed[row1][col1] = True

            os.system('clear')
            print_board(board, revealed)

            row2 = input('Enter the row for the second card (0-3) or q to return to the main menu: ')
            if row2.lower() == 'q':
                revealed[row1][col1] = False
                return False
            row2 = int(row2)
            col2 = int(input('Enter the column for the second card (0-3): '))
            if revealed[row2][col2]:
                print("Card already revealed. Choose another card.")
                revealed[row1][col1] = False
                continue
            revealed[row2][col2] = True

            os.system('clear')
            print_board(board, revealed)

            if board[row1][col1] != board[row2][col2]:
                print('No match! Try again.')
                time.sleep(2)  # Pause to let the user see the result
                revealed[row1][col1] = False
                revealed[row2][col2] = False
            else:
                print('Match found!')
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter numbers between 0 and 3.")
    return True

# Function to start the game
def start_game():
    board = [symbols[:4], symbols[4:8], symbols[8:12], symbols[12:]]
    revealed = [[False]*4 for _ in range(4)]
    start_time = time.time()
    while not all(all(row) for row in revealed):
        os.system('clear')
        print_board(board, revealed)
        if not get_card_selection(board, revealed):
            return
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Congratulations! You've found all matches in {duration} seconds.")
    save_score(duration)

# Function to save the score to the leaderboard
def save_score(duration):
    name = input("Enter your name for the leaderboard: ")
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{duration}\n")

# Function to display instructions
def display_instructions():
    os.system('clear')
    print("📜 Memory Game Instructions:")
    print("1. The game board contains pairs of hidden symbols.")
    print("2. On each turn, you can reveal two cards.")
    print("3. If the symbols on the cards match, they remain revealed.")
    print("4. If they do not match, they will be hidden again.")
    print("5. The game continues until all pairs are matched.")
    print("Good luck 🤞") 
    print("\nPress Enter to return to the menu.")
    input()  # Waits for the user to press Enter so that they can go back to the menu

# Function to display about information
def display_about():
    os.system('clear')
    print("📜 About Memory Game:")
    print("Version: 1.0")
    print("Author: NegPod 9")
    print("This game is a simple memory matching game developed as a project that aims to support cognitive health for all in Africa and beyond.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter

# Function to display the leaderboard
def display_leaderboard():
    os.system('clear')
    print("🏆 Leaderboard 🏆")
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            scores = [line.strip().split(",") for line in file]
            scores = sorted(scores, key=lambda x: float(x[1]))
            for i, (name, time) in enumerate(scores):
                print(f"{i+1}. {name} - {time} seconds")
    else:
        print("No scores available yet.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter

# The menu interface 
def display_menu():
    while True:
        os.system('clear')
        terminal_width = shutil.get_terminal_size().columns
        border = '+' * terminal_width

        print(border)
        print("\033[1m\033[34m" + "✨   Welcome to the Memory Game ✨".center(terminal_width) + "\033[0m")
        print(border)
        print("1. Start Game")
        print("2. View Leaderboard")
        print("3. Instructions")
        print("4. About")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            time.sleep(2)  # gives two seconds for the user to give their choice

# Main program logic
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            print("Starting the game...")
            start_game()
        elif choice == '2':
            display_leaderboard()
        elif choice == '3':
            display_instructions()
        elif choice == '4':
            display_about()
        elif choice == '5':
            print("Exiting the game. Goodbye!")
            break
        input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()

