from .jeuDomino import JeuDomino
class Statistic :
    NOMBRE_DE_LANCER = 10000

    def __init__(self, jeuDomino : JeuDomino):
        self.jeuDomino = jeuDomino
        self.tabX = [] # Tableau des nb_domino_place
        self.tabY = [] # Tableau des points restant
        self.lancer_jeu_domino(self.NOMBRE_DE_LANCER)

    def lancer_jeu_domino(self, nb_lancer : int):
        """Lancer nb_lancer fois le jeu de domino et récupère les stats

        Args:
            nb_lancer (int): nombre de fois que l'on veut lancer le jeu de domino 
        """
        for i in range(nb_lancer):
            x, y = self.jeuDomino.nouveauJeu(False)
            self.tabX.append(x)
            self.tabY.append(y)
    
    def loi_de_probabilite_X(self):
        """Détermine la loi de probabilité de X
        """

        tabX = [0 for i in range(max(self.tabX)+1)]
        for nb_domino_place in self.tabX:
            tabX[nb_domino_place] += 1
        
        tabX = [occurence/self.NOMBRE_DE_LANCER for occurence in tabX]
        print(tabX)
        print(len(tabX))

    def loi_de_probabilite_Y(self):
        """Détermine la loi de probabilité de X
        """

        tabY = [0 for i in range(max(self.tabY)+1)]
        for somme_point_pioche in self.tabX:
            tabY[somme_point_pioche] += 1
        
        tabY = [occurence/self.NOMBRE_DE_LANCER for occurence in tabY]
        print(tabY)
        print(len(tabY))
        print(max(self.tabY))

    def esperance_X(self):
        esperance = self.esperance(self.tabX)
        print(esperance)
    
    def esperance_Y(self):
        esperance = self.esperance(self.tabY)
        print(esperance)

    def esperance(self, tab):
        esperance = sum(tab)/self.NOMBRE_DE_LANCER
        return esperance
    
    def variance_X(self):
        self.ecart_type()

    def ecart_type(self):
        return