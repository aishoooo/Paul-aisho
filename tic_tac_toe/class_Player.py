class Player:
    def init(self, symbol):
        self.points = 0
        self.symbol = symbol
        self.name = input('Entrez le nom de votre joueur : ')
        while self.name == "":
            print("Veuiller mettre un nom")
            self.name = input('Entrez le nom de votre joueur : ')



    def choice_player(self):
        line= input('choississez la ligne(entre 0 et 2) : ')
        column= input('choississez la colonne(entre 0 et 2): ')

        valid_list = ["0", "1", "2"]

        while line not in valid_list or column not in valid_list:
            print("Vous vous êtes trompés choisissez bien un chiffre entre 0 et 2")
            line= input('choississez la ligne : ') 
            column= input('choississez la colonne : ')
        return int(line), int(column)
        
        
