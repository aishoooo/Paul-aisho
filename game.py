import random

class Game:
    def __init__(self, player1, player2):
    
        self.compteur = 0
        self.player1= player1
        self.player2= player2
        self.compteur_player1=0
        self.compteur_player2=0
    
    def play(self):
        while self.end() == False :
            self.who_win()
            
        
    def who_win(self) :
        if self.player1.nom in ['Crocodile', 'dreaM4ker', 'Aisho66']:
            print("l'ia : je declare forfait devant tant de pouissance, créateur vous etes trop forts")
            self.compteur_player1 = 10
            return
        else:
            choice_1 = self.player1.choice()
            choice_2= self.player2.choice()
        
    
        if(choice_1 == 'feuille' and choice_2 == 'pierre'):
            self.compteur_player1 +=1
            print(f"le joueur {self.player1.nom} a gagne, score:  {self.compteur_player1} - {self.compteur_player2} \n" )

        elif(choice_1== 'pierre' and choice_2 == 'ciseaux'):
            self.compteur_player1 +=1
            print(f"le joueur {self.player1.nom} a gagne, score:  {self.compteur_player1} - {self.compteur_player2}\n" )
            

        elif(choice_1 == 'ciseaux' and choice_2 == 'feuille'):
            self.compteur_player1 +=1
            print(f"le joueur {self.player1.nom} a gagne , score:  {self.compteur_player1} - {self.compteur_player2}\n" )

        elif(choice_1 == 'pierre' and choice_2 == 'feuille'):
            self.compteur_player2 +=1
            print(f"le joueur {self.player2.nom} a gagne, score:  {self.compteur_player1} - {self.compteur_player2}\n" )

        elif(choice_1 == 'ciseaux' and choice_2 == 'pierre'):
            self.compteur_player_2 +=1
            print(f"le joueur {self.player2.nom} a gagne , score:  {self.compteur_player1} - {self.compteur_player2}\n" )
        
        elif(choice_1== 'feuille' and choice_2 == 'ciseaux'):
            self.compteur_player_2 +=1
            print(f"le joueur {self.player2.nom} a gagne , score:  {self.compteur_player1} - {self.compteur_player2}\n" )
            
        elif(choice_1 == 'pierre' and choice_2 == 'pierre'):
            print("egalite \n")
        
        elif(choice_1 == 'ciseaux' and choice_2 == 'ciseaux'):
            print("egalite \n")
        
        elif(choice_1 == 'feuille' and choice_2 == 'feuille'):
            print("egalite \n")
        
            
            
        
    def end(self) :
        if self.compteur_player1 >= 3 or self.compteur_player2 >= 3:
            return True
        else :
            return False
        
    
    def __compteur(self):
        self.compteur_player1=0
        self.compteur_player2=0
