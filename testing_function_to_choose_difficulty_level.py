import random
import os
import time

 # List of symbols for the cards 
symbols = ['🤎','🤩','🤑','🤡','😎','😂','😏','🥵']
symbols = symbols * 2 #to make pairs 

 #to shuffle the symbols randomly 
random.shuffle(symbols)

#List of numbers for the cards
numbers = ['2','4','6','8','10','12','14','16']
numbers = numbers * 2 #to make pairs 
random.shuffle(numbers)

#List of letters for the cards 
letters = ['A','F','H','U','L','T','C','Z']
letters = letters * 2 #to make pairs
random.shuffle(letters)

#Output the shuffled lists
print("Shuffled Symbols:", symbols)
print("Shuffled Numbers:", numbers)
print("Shuffled Letters:", letters)

# Function to print the board
def print_board(board, revealed):
    for i in range(4):
        for j in range(4):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('❓ ', end=' ')
        print()

# Function to get the player's card selection
def get_card_selection(board, revealed):
    # Get the first card
    row1 = int(input('Enter the row for the first card (0-3): '))
    col1 = int(input('Enter the column for the first card (0-3): '))
    revealed[row1][col1] = True

    os.system('clear')  # Use 'cls' if you're on Windows
    print_board(board, revealed)

    # Get the second card
    row2 = int(input('Enter the row for the second card (0-3): '))
    col2 = int(input('Enter the column for the second card (0-3): '))
    revealed[row2][col2] = True

    os.system('clear')  # Use 'cls' if you're on Windows
    print_board(board, revealed)

    # Check if the cards match
    if board[row1][col1] != board[row2][col2]:
        print('No match! Try again.')
        time.sleep(2)  # Pause to let the user see the result
        revealed[row1][col1] = False
        revealed[row2][col2] = False
    else:
        print('Match found!')

#The menu interface 
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
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            time.sleep(2)  # gives two seconds for the user to give their choice

display_menu()

#The function that is linked to 2.Instructions
def display_instructions():
    os.system('clear')
    print("📜 Memory Game Instructions:")
    print("1. The game board contains 8 pairs of hidden symbols.")
    print("2. On each turn, you can reveal two cards.")
    print("3. If the symbols on the cards match, they remain revealed.")
    print("4. If they do not match, they will be hidden again.")
    print("5. The game continues until all pairs are matched.")
    print("Goodluck 🤞") 
    print("\nPress Enter to return to the menu.")
    input()  # Waits for the user to press Enter sp that they can go back to the menu

#The fuction that is linked to 3.about
def display_about():
    os.system('clear')
    print("📜 About Memory Game:")
    print("Version: 1.0")
    print("Author: NegPod 9")
    print("This game is a simple memory matching game developed as a project that aims to support cognitive health for all in Africa and beyond.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter

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