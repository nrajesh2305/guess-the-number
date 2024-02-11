
import random

website_url = "" # Replace later with portfolio project website when finished.

random_number = -1
num_lives = 10
isVictory = False

def printIntro():
    print("Guess the Number, by Nithin Rajesh " + website_url + "\n\nI am thinking of a number between 1 and 100.")

def generateRandomNumber():
    random_number = random.randint(1, 100)
    return random_number

def checkGuess(guess):
    if guess > random_number:
        return "Your guess is too high."
        num_lives -= 1
    elif guess < random_number:
        return "Your guess is too low."
        num_lives -= 1
    else:
        return "Yay! You guessed the number!"
        isVictory = True
        