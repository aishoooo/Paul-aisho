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
        #self.compteur_player_1=0
        #self.compteur_player_2=0
    
    def play(self, player):
        while b == False:
            ligne_1, colone_1 = self.player_1.choice_player() 
            self.board[ligne_1][colone_1]= 1
            self.board_front[ligne_1][colone_1]= 'X'
            for i in self.board_front:
                print(i)
        # while self.board[ligne_1] != 0 and self.board[colone_1] !=0:
        #     print ('tu t es trompé')
        #     self.player_1.choice_player() 
            ligne_2, colone_2 = self.player_2.choice_player() 
            self.board[ligne_2][colone_2]= 2
            self.board_front[ligne_2][colone_2]= 'O'
            for i in self.board_front :
                print(i)
                while self.board[ligne_2] != 0 and self.board[colone_2] !=0:
            #     print ('tu t es trompé')
            #     self.player_2.choice_player()
            #while choice_player_1 == True:
            #    print ('au tour du player 2')
            #    return choice_player1
            
            

    def win (self, board, player):
        if (board[0][0] == player and board[1][0] == player  and board [2][0] == player ) :
            print ("WIN")
            
            self.compteur_player +=1
            return(True)
        elif (board[0][1]== player and board[1][1] == player  and board [2][0] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        elif (board[0][2]== player and board[1][2] == player  and board [2][2] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        elif (board[0][0]== player and board[1][1] == player  and board [1][2] == player ):
            print ("WIN")
            return (True)
        elif (board[1][0]== player and board[1][1] == player  and board [1][2] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        elif (board[2][0]== player and board[2][1] == player  and board [2][2] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        elif (board[0][0]== player and board[1][1] == player  and board [2][2] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        elif (board[0][1]== player and board[1][1] == player  and board [0][2] == player ):
            print ("WIN")
            self.compteur_player +=1
            return (True)
        return (False)
    
    def end(self) :
        if self.compteur_player1 >= 3 or self.compteur_player2 >= 3:
            return True
        else :
            return False

player_1 = Player()
player_2 = Player()
a = morpion(player_1, player_2)
b = morpion.win() 
#for i in a.board_front:
#    print(i)
#a.player2.choice_player()
#for i in a.board_front:
#    print(i)

a.play()