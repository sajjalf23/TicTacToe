class TikTakToe :
    first_player = "X"
    second_player = "O"

    def __init__(self):
        self.board = [
            [" " , " "  , " "],
            [" " ,  " " , " "],
            [" " ,  " " , " "]
        ]
        self.current_player = 1

    def display(self):
        print("\n\n")
        print(" <<<<< Here is the board >>>>")
        for row in self.board :
            print("   " , row[0] , "  |   " , row[1] , "   |   " , row[2] )
            print("---------------------------")
        print("\n")

    def move(self,row,col):
        if(self.current_player == 1):
            if(self.board[row][col] == " "):
                self.board[row][col] = self.first_player
                self.current_player = 0
        else:
            if(self.board[row][col] == " "):
                self.board[row][col] = self.second_player
                self.current_player = 1
        self.display()
        self.winner()

    def display_winner(self , x):
        if(x == self.first_player):
            print(" <<<< winner >>>> is first player using symbol : " , self.first_player )
        else:
            print(" <<<< winner >>>> is second player using symbol : " , self.second_player )

    def fullboard(self):
        check = 0
        for row in self.board :
            for i in row :
                if(i == " "):
                    check = 1
        if(check == 1):
            row = input("enter row : (0 to 2) ")
            col = input("enter col : (0 to 2) ")
            row = int(row)
            col = int(col)
            self.move(row, col)
        elif(check == 0):
            print(" Draw  ")
            return

    def winner(self):
        if(self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]  and self.board[0][1] != " "):
            self.display_winner(self.board[0][1])
            return
        elif(self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[1][0]  != " "):
            self.display_winner(self.board[1][0])
            return
        elif(self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[1][2]  != " "):
            self.display_winner(self.board[1][2])
            return
        elif(self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][1]  != " "):
            self.display_winner(self.board[2][1])
            return
        elif(self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[1][1]  != " "):
            self.display_winner(self.board[1][1])
            return
        elif(self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][1]  != " "):
            self.display_winner(self.board[1][1])
            return
        elif(self.board[0][0] == self.board[1][1] and  self.board[1][1] == self.board[2][2] and  self.board[1][1] != " "):
            self.display_winner(self.board[1][1])
            return
        elif(self.board[0][2] == self.board[1][1] and  self.board[1][1]  == self.board[2][0] and  self.board[1][1]  != " "):
            self.display_winner(self.board[1][1])
            return
        else:
            self.fullboard()
    


T1 = TikTakToe()
T1.display()
row = input("enter row number to start (0 to 2) : ")
col = input("enter col number to start (0 to 2) : ")
row = int(row)
col = int(col)
T1.move(row,col)