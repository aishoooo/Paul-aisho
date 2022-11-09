from class_Player import Player

class morpion:
    def __init__(self, player_1, player_2):
        self.board = [
            [0, 0, 0,],
            [0, 0, 0,],
            [0, 0, 0,]
        ]
        self.board_front = [
            ['', '', '',],
            ['', '', '',],
            ['', '', '']
        ]
        self.player_1 = player_1
        self.player_2 = player_2

    def play(self):
      
        end = False
        while not end:
            for player in [self.player_1,self.player_2]:
                line_1, column_1 = player.choice_player() 
                while self.board[line_1][column_1] != 0:
                    print ('tu t es trompé')
                    line_1, column_1 = player.choice_player()
                self.board[line_1][column_1]= player.symbol
                self.board_front[line_1][column_1]= player.symbol
                for i in self.board_front:
                    print(i)
                end = self.__win(player)
                if end:break

            
           
            

    def __win(self, player):
        if (self.board[0][0] == player.symbol and self.board[1][0] == player.symbol  and self.board[2][0] == player.symbol ) :
            print (player.nom + " a gagné")
            return(True)
        elif (self.board[0][1]== player.symbol and self.board[1][1] == player.symbol  and self.board[2][0] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[0][2]== player.symbol and self.board[1][2] == player.symbol  and self.board[2][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[0][0]== player.symbol and self.board[1][1] == player.symbol  and self.board[1][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[1][0]== player.symbol and self.board[1][1] == player.symbol  and self.board[1][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[2][0]== player.symbol and self.board[2][1] == player.symbol  and self.board[2][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[0][0]== player.symbol and self.board[1][1] == player.symbol  and self.board[2][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        elif (self.board[0][1]== player.symbol and self.board[0][0] == player.symbol  and self.board[0][2] == player.symbol ):
            print (player.nom + " a gagné")
            return (True)
        return (False)
    

player_1 = Player('X')
player_2 = Player('O')
a = morpion(player_1, player_2)
#for i in a.board_front:
#    print(i)
#a.player2.choice_player()
#for i in a.board_front:
#    print(i)

a.play()