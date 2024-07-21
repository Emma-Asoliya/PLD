 import random

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

#The menu interface 


