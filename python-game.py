import random

number = random.randint(1, 100)
game_over = False

username = input("Hello, What is your username? ")

print("hello", username + ".", )

question = input("would you like to play a game? [Y/N] " )

if question == "n":
    print("oh.. okay")
if question == "y":
    print("okay, I'm thinking of a number between 1 and 100")
    while game_over == False:

        guess = int(input("have a guess: "))
        if guess > number:
            print("too high!")
        if guess < number:
            print("too low!")
        if guess == number:
            print("correct!")
            game_over == True
            break
    
 
    



