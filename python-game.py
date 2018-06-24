import random

number = random.randint(1, 10)
tries = 1

username = input("Hello, What is your username?")

print ("hello", username + ".",)

question = input("would you like to play a game? [Y/N] " )

if question == "n":
    print("oh.. okay")
if question == "y":
    print("okay, I'm thinking of a number between 1 and 5")
    guess = int(input("have a guess:"))
    if guess > number:
        print("too high")
    if guess < number:
        print("too low")
    if guess == number:
        print("You got it right! the correct number was", number + \
        "Great Guess!")

