import string
import random


def randomPassword(num):
    randomSource = string.ascii_letters + string.digits + string.punctuation
    passString = random.choice(string.ascii_lowercase)
    passString += random.choice(string.digits)
    passString += random.choice(string.ascii_uppercase)
    passString += random.choice(string.punctuation)

    for i in range(num):
        passString += random.choice(randomSource)

    passwordList = list(passString)
    random.SystemRandom().shuffle(passwordList)
    passString = "".join(passwordList)

    print(passString)


randomPassword(20)
