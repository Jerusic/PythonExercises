class Player:
    def __init__(self, name="", throwChoice=""):
        self.name = name
        self.throwChoice = throwChoice

    def getName(self):
        return self.name

    def getThrowChoice(self):
        return self.throwChoice

    def setName(self, name):
        self.name = name

    def setThrowChoice(self, throwChoice):
        self.throwChoice = throwChoice

def chooseThrow(playerName):
    playerChoice = ""
    while not (playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors"):
        playerChoice = input("\n" + playerName.getName() + ", what do you throw? ")
        playerChoice = playerChoice.lower()
    return playerChoice

def evaluate(player1, player2):
    if player1.getThrowChoice() == player2.getThrowChoice():
        print("It's a tie! Both players chose " + player1.getThrowChoice())        
    elif player1.getThrowChoice() == "rock" and player2.getThrowChoice() =="scissors" or \
         player1.getThrowChoice() == "scissors" and player2.getThrowChoice() =="paper" or \
         player1.getThrowChoice() == "paper" and player2.getThrowChoice() =="rock":
        print(player1.getName() + " wins by choosing " + player1.getThrowChoice() + \
              " to beat " + player2.getName() + "\'s " + player2.getThrowChoice())        
    else:
        print(player2.getName() + " wins by choosing " + player2.getThrowChoice() + \
              " to beat " + player1.getName() + "\'s " + player1.getThrowChoice())
        
def contPlay():
    quitOrCont = input("Enter \'q\' to quit, \'n\' to assign new players, or anything else to continue playing: ")
    quitOrCont = quitOrCont.lower()
    if quitOrCont == "q":
        print("\nGoodbye!")
        return False
    elif quitOrCont == "n":
        return ("n")
    else:
        print("\nNew Game!")
        return True

def main():
    print("Let's play rock, paper, scissors!")
    while True:
        player1Name = input("Enter first player name: ")
        player2Name = input("Enter second player name: ")
        player1 = Player(player1Name)
        player2 = Player(player2Name)
        newGame = True
        print("Please enter \'rock\', \'paper\', or \'scissors\'.")
        while newGame:
            player1.setThrowChoice(chooseThrow(player1)) 
            player2.setThrowChoice(chooseThrow(player2)) 
            evaluate(player1, player2)
            newGame = contPlay()
            if newGame == "n": break
        if newGame == False: break
        
main()
