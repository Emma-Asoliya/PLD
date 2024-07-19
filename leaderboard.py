#!/usr/bin/python3
import os

LEADERBOARD_FILE = "leaderboard.txt"

# Function to update the leaderboard
def update_leaderboard(player_name, elapsed_time):
     with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{player_name},{elapsed_time}\n")

# Function to display the leaderboard
def display_leaderboard():
    os.system('clear')
    print("🏆 Leaderboard 🏆")
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            scores = [line.strip().split(",") for line in file]
            scores = sorted(scores, key=lambda x: float(x[1]))
            for i, (name, time) in enumerate(scores):
                print(f"{i+1}. {name} - {time} seconds")
    else:
        print("No scores available yet.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter
