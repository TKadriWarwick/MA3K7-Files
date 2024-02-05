import numpy as np

class game:
    def __init__(self, n: int, playerStarts: bool, playerIsZero: bool):
        self.dim = n
        self.playersGo = playerStarts
        self.playerIsZero = playerIsZero

        self.available = [[i,j] for i in range(n) for j in range(n)]
        self.board = [["_" for i in range(n)] for j in range(n)]

    def isClean(self, string: str, arr: list) -> bool:
        clean = False
        temp = string.split()
        if len(temp) == 2 and temp[0].isnumeric() and temp[1].isnumeric():
            coord = [int(i.strip()) for i in string.split()]
            if coord in arr:
                clean = True
        return clean
    
    def printBoard(self) -> None:
        for row in self.board:
            print("[{0}]".format(', '.join(map(str, row))))

    def results(self) -> None:
        det = np.linalg.det(self.board)
        print("The determinant is: " + str(det))
        if det == int(not self.playerIsZero):
            print("Player Wins!")
        else:
            print("Bot Wins.")

    def takePlayerInput(self) -> None:
        x = input("Enter co-ordinate: ")
        while self.isClean(x, self.available) == False:
            x = input("Please enter co-ordinate in correct format: ")
        x = [int(i.strip()) for i in x.split()]
        self.available.remove(x)
        self.board[x[0]][x[1]] = int(not self.playerIsZero)
        self.playersGo = False

    def takeBotInput(self, x: list) -> None:
        print("Bot chooses: " + str(x))
        self.available.remove(x)
        self.board[x[0]][x[1]] = int(self.playerIsZero)
        self.playersGo = True



class randGame(game): # Plays a random move
    def play(self) -> None: 

        self.printBoard()

        while len(self.available) > 0:
            if self.playersGo:
                self.takePlayerInput()
            else:
                num = np.random.randint(0,len(self.available))
                x = self.available[num]
                self.takeBotInput(x)
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
                        num = np.random.randint(0,len(self.available))
                        x = self.available[num]
                        self.takeBotInput(x)

            self.printBoard()


        self.results()
        



if __name__ == "__main__":
    newGame = smarterGame(3, False, True)
    newGame.play()