moveList = []
playerList = []


class Player:
    def __init__(self):
        self.name = input("What is your name? ")
        self.addPlayer(self.name)

    def addPlayer(self, name):
        playerList.append(name)

    def addMove(self):
        move = input(self.name + ", choose Rock, Paper, or Scissor? ")
        move = move.lower()
        if move == 'rock' or move == 'paper' or move == 'scissor':
            moveList.append(move)
        else:
            print('That was not a valid choice.')
            self.addMove()

    def gamePlay(self):
        self.addMove()
        if len(moveList) == 2:
            chooseWinner()


def chooseWinner():
    if moveList[0] == 'rock' and moveList[1] == 'scissor':
        print(playerList[0] + ", Congratulations! You Won!")
    elif moveList[1] == 'rock' and moveList[0] == 'scissor':
        print(playerList[1] + ", Congratulations! You Won!")
    elif moveList[0] == 'paper' and moveList[1] == 'rock':
        print(playerList[0] + ", Congratulations! You Won!")
    elif moveList[1] == 'paper' and moveList[0] == 'rock':
        print(playerList[1] + ", Congratulations! You Won!")
    elif moveList[0] == 'scissor' and moveList[1] == 'paper':
        print(playerList[0] + ", Congratulations! You Won!")
    elif moveList[1] == 'scissor' and moveList[0] == 'paper':
        print(playerList[1] + ", Congratulations! You Won!")


ned = Player()
barbara = Player()
ned.gamePlay()
barbara.gamePlay()
