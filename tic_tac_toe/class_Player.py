class Player:
    def __init__(self, symbol):
        self.points = 0
        self.symbol = symbol
        self.nom = input('Entrez le nom de votre joueur : ')
        while self.nom == "":
            print("Veuiller mettre un nom")
            self.nom = input('Entrez le nom de votre joueur : ')
        

    
    def choice_player(self):
        line= input('choississez la line : ')
        column= input('choississez la column : ')
        
        valid_list = ["0", "1", "2"]
        
        while line not in valid_list or column not in valid_list:
            print("Choississez entre 0 et 2")
            line= input('choississez la line : ') 
            column= input('choississez la column : ')  
        return int(line), int(column)
       
    
        
        
        
        