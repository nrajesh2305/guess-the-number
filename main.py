import random

website_url = "" # Replace with your portfolio project website later when done.

print("Guess the Number, by Nithin Rajesh " + website_url + "\n\n")
secret_number = random.randint(1, 100)
num_lives = 10
guess = -1
isVictory = False

while guess != secret_number and num_lives != 0:
    if num_lives == 0:
        break
    guess = int(input(f"You have {num_lives} guesses left. Take a guess.\n> "))
    if(guess > secret_number):
        num_lives -= 1
        print("Too high!")
    elif guess < secret_number:
        num_lives -= 1
        print("Too low!")
    else:
        isVictory = True
        break

if isVictory:
    print("Yay! You guessed my number.")
else:
    print("Game Over! The number I was thinking of was " + str(secret_number) + ".")
