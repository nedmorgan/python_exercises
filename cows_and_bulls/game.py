import random
import re

randomNumber = str(random.randint(1000, 9999))
print("Welcome to the Cows and Bulls Game!")

def inputNumber():
  playerInput = input("Enter a 4 digit number: ")
  if len(playerInput) != 4:
    if hasLetters(playerInput) == True:
      print("Please do not input letters")
      inputNumber()
    else:
      inputNumber()
  elif len(playerInput) == 4:
    if hasLetters(playerInput) == True:
      print("Please do not input letters")
      inputNumber()
    else:
      checkNumber(playerInput)

def checkNumber(inputNum):
  num = splitString(inputNum)
  compNum = splitString(randomNumber)
  if num == compNum:
    print("Congratulations! You guess correct!")
  else:
    compare(num, compNum)

def compare(myNum, computerNum):
  cow = 0
  bull = 0
  for i in range (4):
    if myNum[i] == computerNum[i]:
      cow = cow + 1
    else:
      for num in computerNum:
        if num == myNum[i]:
          bull = bull + 1
  print(str(cow) + " cows, " + str(bull) + " bulls")
  inputNumber()

def splitString(str):
  return [char for char in str]

def hasLetters(str):
  return bool(re.match('[a-zA-Z]', str))

inputNumber()

