# Define global variables for the game
gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # 0 index unused
player1 = {"name": "", "symbol": "X"}
player2 = {"name": "", "symbol": "O"}

# Define print function for game board
def printboard():
    print(f"{gameboard[7]} | {gameboard[8]} | {gameboard[9]}")
    print("--+---+--")
    print(f"{gameboard[4]} | {gameboard[5]} | {gameboard[6]}")
    print("--+---+--")
    print(f"{gameboard[1]} | {gameboard[2]} | {gameboard[3]}")

# Method for set-up (player names, symbols, etc.)
def playersetup():
    player1set = False

    while player1set == False:
        nameinput = input("Welcome to Tic Tac Toe! Please enter Player 1's name: ")
        if not nameinput.isalnum() or nameinput.isspace():
            print("Invalid name. Please use only letters and numbers.")
        else:
            player1["name"] = nameinput
            player1set = True

    player2set = False

    while player2set == False:
        nameinput = input("Please enter Player 2's name: ")
        if not nameinput.isalnum() or nameinput.isspace():
            print("Invalid name. Please use only letters and numbers.")
        else:
            player2["name"] = nameinput
            player2set = True

    input(f"{player1["name"]}, you will be Xs. {player2["name"]}, you will be Os. Press Enter to start the game!")

# Method for player moves
def playermove(playername, symbol):
    validmove = False

    while validmove == False:
        move = input(f"{playername}, please enter the number of the square where you want to place your {symbol} (1-9): ")
        if gameboard[int(move)] == " ":
            validmove = True
            gameboard[int(move)] = symbol
        else:
            print("That space is already taken. Try a different space.")
        

# Function to check for a win or draw condition
def checkwin():
    # Check rows
    if (gameboard[1] == gameboard[2] == gameboard[3] != " ") or \
       (gameboard[4] == gameboard[5] == gameboard[6] != " ") or \
       (gameboard[7] == gameboard[8] == gameboard[9] != " "):
        return True

    # Check cols
    if (gameboard[1] == gameboard[4] == gameboard[7] != " ") or \
       (gameboard[2] == gameboard[5] == gameboard[8] != " ") or \
       (gameboard[3] == gameboard[6] == gameboard[9] != " "):
        return True

    # Check diagonals
    if (gameboard[1] == gameboard[5] == gameboard[9] != " ") or \
       (gameboard[3] == gameboard[5] == gameboard[7] != " "):
        return True
    
    return False

# Function to check for a draw condition
def checkdraw():
    for i in range(1, 10):
        if gameboard[i] == " ":
            return False
    return True       

# Method for swapping player turns
def swap(selectedplayer):
    if selectedplayer == player1:
        return player2
    elif selectedplayer == "":
        return player1
    else:
        return player1

# Main method for executing game
def execgame():
    playersetup()
    currplayer = ""

    while checkwin() == False and checkdraw() == False:
        currplayer = swap(currplayer)
        printboard()
        playermove(currplayer["name"], currplayer["symbol"])
        
    if(checkwin()):
        print(f"Congrats {currplayer["name"]}, you've won!")
        printboard()
    elif(checkdraw()):
        print("The game ended in a draw!")
        printboard()

def main():
    playerdesire = True

    while playerdesire == True:
        execgame()

        playerdesireinput = input("Would you like to play again? (y/n): ")
        if playerdesireinput.lower() == "y":
            global gameboard
            gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # Reset gameboard
            playerdesire = True
        else:
            playerdesire = False
            print("Thanks for playing!")

main()