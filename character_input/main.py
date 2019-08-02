import datetime


def ageAtHundred():
    now = datetime.datetime.now()
    currentYear = now.year
    inputName = askName()
    inputAge = askAge()
    diffFromHundred = 100 - int(inputAge)
    yearAtHundred = diffFromHundred + currentYear
    print("Your name is " + inputName +
          " and you will be 100 years old in the year " + str(yearAtHundred))


def askName():
    newName = input("What is your name? ")
    return newName


def askAge():
    newAge = input("What is your age? ")
    return newAge


ageAtHundred()
