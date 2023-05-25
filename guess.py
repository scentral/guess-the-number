import random

generate_number = random.randint(1, 10)
guess = None

while guess != generate_number:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == generate_number:
        print("You got it!")
        break
    else:
        print("You got it wrong!")