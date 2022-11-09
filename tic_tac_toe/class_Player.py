class Player:

    def __init__(self):
        self.nom = input('Entrez le nom de votre joueur : ')

    def choice_player(self):
        ligne= int(input('choississez la ligne : ')) 
        colone= int(input('choississez la colonne : ')) 
        return ligne, colone
        
        
        
        
        