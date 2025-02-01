import random
def GuessNumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    number = random.randint(1, 20)
    att = 0
    guess = None
    while guess != number:
        guess = int(input())
        att += 1
        if guess < number:
            print("Your guess is too low.\nTake a guess.")
        elif guess > number:
            print("Your guess is too high.\nTake a guess.")
    print(f"Good job, {name}! You guessed my number in {att} guesses!")   
GuessNumber()