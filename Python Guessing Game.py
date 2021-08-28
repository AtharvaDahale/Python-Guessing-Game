# Random Number Guessing Game

import random

flag = True
while flag:
    num = input("Type a number to guess between 1 and ")
    
    if num.isdigit():
        print("Let's Play!")
        num = int(num)
        flag = False
    else:
        print("Invalid Input! Try Again!")
        

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    print("The computer has guessed a number between 1 and " + str(num))
    guess = input("The number between 1 and " + str(num) + " is- ")
    if guess.isdigit():
        guess = int(guess)
        
    if guess == secret:
        print("You got it!")
    else:
        print("Please try again!")
        count += 1
        
print("It took you", count, "attempts to guess the right number!")