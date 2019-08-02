def fibonacci(num):
    firstNum = 0
    secondNum = 1
    increment = 2
    if num < 0:
        print("Incorrect Input")
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    elif num > 2:
        sequence = [0, 1]
        while len(sequence) != num:
            indexOne = increment - 2
            indexTwo = increment - 1
            nextNum = sequence[indexOne] + sequence[indexTwo]
            sequence.append(nextNum)
            increment += 1
        return sequence
