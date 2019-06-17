
import random
import time

number = random.randint(1,100)
guess_limit = 5

print("Welcome to the guessing game!\n")

while True:
    guess = int(input("Predict a number from 1-100:\n"))
    
    if guess == number:
        time.sleep(1)
        print("Congratulations! Correct guess!\n")
        break
    
    elif guess > number:
        time.sleep(1)
        guess_limit = guess_limit - 1
        print("\nGuess smaller\n")
        print("Remaining guess:\n", guess_limit)
    
    else:    
        time.sleep(1)
        guess_limit = guess_limit - 1
        print("\nGuess bigger\n")
        print("Remaining guess:", guess_limit)
        
    if guess_limit == 0:
        print("Sorry, you lost the game!\n")
        print("Correct number was:", number)
        break
