class ia:
    
    def __init__(self, stats, ia_choice):
        #self.stats = [pierre = 0.35, feuille = 0.30, ciseaux = 0.35]
        self.stats = {"pierre" : 0.35,
                      "feuille" : 0.30,
                      "ciseaux" : 0.35, 
                      }
        self.ia_choice = 'pierre','feuille','ciseaux'
      
    
    def choice():
        return min(self.stats)
    