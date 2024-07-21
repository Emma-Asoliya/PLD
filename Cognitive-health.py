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



