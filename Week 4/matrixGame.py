import numpy as np

class game:
    def __init__(self, n: int, playerStarts: bool, playerIsZero: bool):
        self.dim = n
        self.playerStarts = playerStarts
        self.playersGo = playerStarts
        self.playerIsZero = playerIsZero

        self.reset()

        self.dimThree = [ # Encoded formula for n=3
            [[0,0], [1,1], [2,2]],
            [[0,1], [1,2], [2,0]],
            [[0,2], [1,0], [2,1]],
            [[0,0], [1,2], [2,1]],
            [[0,1], [1,0], [2,2]],
            [[0,2], [1,1], [2,0]]
        ]

    def isClean(self, string: str, arr: list) -> bool: # Checks player input
        clean = False
        temp = string.split()
        if len(temp) == 2 and temp[0].isnumeric() and temp[1].isnumeric():
            coord = [int(i.strip()) for i in string.split()]
            if coord in arr:
                clean = True
        return clean
    
    def printBoard(self) -> None: # Prints the matrix
        for row in self.board:
            print("[{0}]".format(', '.join(map(str, row))))

    def results(self) -> None: # Shows who is the winner
        det = np.linalg.det(self.board)
        print("The determinant is: " + str(det))
        if det == int(not self.playerIsZero):
            print("Player Wins!")
        else:
            print("Bot Wins.")

    def takePlayerInput(self) -> None: # Takes player imput until it's in the right format
        x = input("Enter co-ordinate: ")
        while self.isClean(x, self.available) == False:
            x = input("Please enter co-ordinate in correct format: ")
        x = [int(i.strip()) for i in x.split()]
        self.available.remove(x)
        self.board[x[0]][x[1]] = int(not self.playerIsZero)
        self.playersGo = False

    def takeBotInput(self, x: list) -> None: # Takes bot input
        print("Bot chooses: " + str(x))
        self.available.remove(x)
        self.board[x[0]][x[1]] = int(self.playerIsZero)
        self.playersGo = True

    def randomMove(self) -> None: # Makes the bot perform a random move
        num = np.random.randint(0,len(self.available))
        x = self.available[num]
        self.takeBotInput(x)

    def reset(self) -> None: # Resets the matrix to empty
        self.available = [[i,j] for i in range(self.dim) for j in range(self.dim)]
        self.board = [["_" for i in range(self.dim)] for j in range(self.dim)]
        self.playersGo = self.playerStarts


class randGame(game): # Plays a random move when its the bots turn
    def play(self) -> None: 

        self.printBoard()

        while len(self.available) > 0:
            if self.playersGo:
                self.takePlayerInput()
            else:
                self.randomMove()
            self.printBoard()
        
        self.results()
                    
        

class smarterGame(game): # Notices if there will be a zero row/column
    def play(self) -> None:
        
        self.printBoard()

        while len(self.available) > 0:
            if self.playersGo:
                self.takePlayerInput()
            else:
                found = False
                x = None

                for i in range(self.dim): # Checks rows
                    count = 0
                    for j in range(self.dim):
                        if self.board[i][j] == 0:
                            count += 1
                        elif self.board[i][j] == "_":
                            x = [i,j]
                    if (count == self.dim -1) and (x != None):
                        self.takeBotInput(x)
                        found = True
                        break

                if not found: 
                    for i in range(self.dim): # Checks columns
                        count = 0
                        for j in range(self.dim):
                            if self.board[j][i] == 0:
                                count += 1
                            elif self.board[j][i] == "_":
                                x = [j,i]
                        if (count == self.dim -1) and (x != None):
                            self.takeBotInput(x)
                            found = True
                            break

                    if not found:
                        self.randomMove()

            self.printBoard()

        self.results()
        


class smartestGame(game): # Uses all strategies discussed in the rubric
    def play(self) -> None:

        self.printBoard()

        if not self.playerIsZero and self.dim == 3: # Uses the "follow" strategy for n=3
            while len(self.available) > 0:
                if self.playersGo:
                    self.takePlayerInput()
                elif len(self.available) == 9: # Plays a random move if going first
                    self.randomMove()
                else:
                    best = []
                    found = False
                    for trip in self.dimThree:
                        count = 0
                        for x in trip:
                            if self.board[x[0]][x[1]] == 0:
                                count = 0
                                break
                            if self.board[x[0]][x[1]] == 1:
                                count += 1
                            elif self.board[x[0]][x[1]] == "_":
                                best = x
                        if count == 2:
                            found = True
                            self.takeBotInput(best)
                            break
                    if found == False:
                        self.takeBotInput(best)
                self.printBoard()

        elif not self.playerIsZero and self.dim > 3: # Uses first two / last two comlumn strategy

            specialCol1 = self.dim-2
            specialCol2 = self.dim-1

            while len(self.available) > 0:
                if self.playersGo:
                    self.takePlayerInput()
                else:
                    found = False
                    for i in [0,1,specialCol1,specialCol2]:
                        for j in range(self.dim):
                            if i == 0 or i == specialCol1:
                                altI = i + 1
                            else:
                                altI = i - 1
                            if self.board[j][i] == 1 and self.board[j][altI] == "_":
                                x = [j, altI]
                                found = True
                                self.takeBotInput(x)
                    if found == False:
                        x = []
                        for i in range(self.dim):
                            i = (i + 2) % self.dim
                            for j in range(self.dim):
                                if self.board[j][i] == "_":
                                    x = [j, i]
                                    break
                            if x != []:
                                self.takeBotInput(x)
                                break
                self.printBoard()

        elif not self.playerIsZero and self.dim == 2: # Hard coded the n=2 case
            while len(self.available) > 0:
                if self.playersGo:
                    self.takePlayerInput()
                elif len(self.available) == 4:
                    self.takeBotInput([0,0])
                elif len(self.available) == 3:
                    if [0,0] not in self.available:
                        self.takeBotInput([1,1])
                    elif [0,1] not in self.available:
                        self.takeBotInput([1,0])
                    elif [1,0] not in self.available:
                        self.takeBotInput([0,1])
                    else:
                        self.takeBotInput([0,0])
                elif len(self.available) == 2:
                    if self.board[0][0] == 0:
                        if self.board[0][1] == 1:
                            x = [1,0]
                        else:
                            x = [0,1]
                    elif self.board[0][1] == 0:
                        if self.board[0][0] == 1:
                            x = [1,1]
                        else:
                            x = [0,0]
                    elif self.board[1][0] == 0:
                        if self.board[0][0] == 1:
                            x = [1,1]
                        else:
                            x = [0,0]
                    else:
                        if self.board[0][1] == 1:
                            x = [1,0]
                        else:
                            x = [0,1]
                    self.takeBotInput(x)
                else:
                    self.randomMove()
                self.printBoard()



        else: # Uses the same strategy as smarterGame if the bot is playing as ones
            while len(self.available) > 0:
                if self.playersGo:
                    self.takePlayerInput()
                else:
                    found = False
                    x = None

                    for i in range(self.dim): # Checks rows
                        count = 0
                        for j in range(self.dim):
                            if self.board[i][j] == 0:
                                count += 1
                            elif self.board[i][j] == "_":
                                x = [i,j]
                        if (count == self.dim -1) and (x != None):
                            self.takeBotInput(x)
                            found = True
                            break

                    if not found: 
                        for i in range(self.dim): # Checks columns
                            count = 0
                            for j in range(self.dim):
                                if self.board[j][i] == 0:
                                    count += 1
                                elif self.board[j][i] == "_":
                                    x = [j,i]
                            if (count == self.dim -1) and (x != None):
                                self.takeBotInput(x)
                                found = True
                                break

                        if not found:
                            self.randomMove()

                self.printBoard()

        self.results()
                    


if __name__ == "__main__":
    game1 = smartestGame(5, True, False)
    game2 = smarterGame(4, False, True)
    game3 = randGame(4, False, True)
    game1.play()