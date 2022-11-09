import random
class Player:
    import random
    def __init__(self):
        self.nom = input('Entrez le nom de votre joueur : ')
        
        
        
    def choice(self):
        choice_player = ['pierre', 'feuille', 'ciseaux']
        if self.nom == "ia" :
            dict_stats = {"pierre" : 35,
                         "feuille" : 30,
                          "ciseaux" : 35, 
                          }
            a = random.randint(1,100)
        
            if a <= 35:
                choice = 'pierre'
            
            elif 35< a <=65:
                choice= 'feuille'
        
            elif a > 65 :
                choice= 'ciseaux'
                
        
        else :
            choice = input(" votre choix : ")
            if choice in ['Crocodile', 'dreaM4ker', 'Aisho66']:
                print ( "l'ia : je declare forfait devant tant de pouissance, créateur vous etes trop forts")
            
        return choice
             
        
   