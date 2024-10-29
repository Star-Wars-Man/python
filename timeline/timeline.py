print("Hello Timeline")

# start game
    # 1. game menu
    # 1.1 select number of players
    # 1.2 [bots on/of]
    # 1.3 [dificultly levle]
    # 2. setup new game
    # 2.1 deal starting card to each player
    # 2.2 show instructions (tell how to play game)
    # 2.3 pick starting game
    # 3. play game (player turns)
    # 3.1 starting player turn
    # 3.2 select next player
    # 3.3 take turn
    # 3.4 check if player has won/game is over, if so goto 4
    # 3.5 goto 3.2
    # 4 show who winner is
def timeline():
    print("Starting timeline game")
    showGameMenu()
    setUpNewGame()
    play()
    showWinner()

def showGameMenu():
    print("Game Menu")

def setUpNewGame():
    print("New Game")

def play():
    print("Playing")

def showWinner():
    print("Your the Winner")

timeline()