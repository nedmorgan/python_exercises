def askNumber():
    number = input("Give me a number between 1 and 100: ")
    number = int(number)
    if number < 1 or number > 100:
        print("That number is not within the range.")
        askNumber()
    else:
        if number % 2 == 0:
            print("You have entered an even number.")
        else:
            print("You have entered an odd number.")


askNumber()
