numList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessThanTenList = []


def lessThanTen(list):
    userNum = int(userNumber())
    for item in list:
        if item < userNum:
            lessThanTenList.append(item)
    print("Current numbers less than your number are: ")
    print(*lessThanTenList, sep=", ")


def userNumber():
    num = input("Give me a number: ")
    return num


lessThanTen(numList)
