import random

chosenNumber = random.randint(1, 10)


def guessNumber():
    guessedNumber = input("Guess a number between 1 and 10: ")
    if str(chosenNumber) == guessedNumber:
        print("You guessed right, great job!")
    elif guessedNumber.lower() == 'exit':
        exit()
    elif str(chosenNumber) != guessedNumber:
        print("You guessed wrong :(")
        guessNumber()


guessNumber()
