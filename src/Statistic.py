from .jeuDomino import JeuDomino
from math import sqrt
class Statistic :
    NOMBRE_DE_LANCER = 10000

    def __init__(self, jeuDomino : JeuDomino):
        self.jeuDomino = jeuDomino
        self.tab_val_x = [] # Tableau des nb_domino_place
        self.tab_val_y = [] # Tableau des points restant
        self.lancer_jeu_domino(self.NOMBRE_DE_LANCER)

    def lancer_jeu_domino(self, nb_lancer : int):
        """Lance le jeu de domino et récupère les stats

        Args:
            nb_lancer (int): nombre de fois que l'on veut lancer le jeu de domino 
        """
        for i in range(nb_lancer):
            x, y = self.jeuDomino.nouveauJeu(False)
            self.tab_val_x.append(x)
            self.tab_val_y.append(y)
    
    @staticmethod
    def loi_de_probabilite(tab_val : list[int], nb_lancer : int) -> list[float] :
        """Calcule la loi de probabilite d'une variable aléatoire

        Args:
            tab_val (list[int]): Valeurs prises par la variable aléatoire
            nb_lancer (int): Nombre de lancer

        Returns:
            list[float]: Loi de probabilite sous la forme loi[valeurEntiere] = probabilite que la valeur soit prise par la variable aléatoire
        """
        loi = [0 for i in range(max(tab_val)+1)]
        for nb_domino_place in tab_val:
            loi[nb_domino_place] += 1
        
        loi = [occurence/nb_lancer for occurence in loi]
        return loi

    @staticmethod
    def esperance(tab_val : list[int], nb_lancer : int) -> float :
        """Calcul l'esperance d'une variable aléatoire

        Args:
            tab_val (list[int]): Valeurs prises par la variable aléatoire
            nb_lancer (int): Nombre de lancer de partie

        Returns:
            float: Esperance de la variable aléatoire
        """
        esperance = sum(tab_val)/nb_lancer
        return esperance
    
    @staticmethod
    def variance(tab_val : list[int], moyenne : float, nb_lancer : int) -> float :
        """Calcule la variance d'une variable aléaoire

        Args:
            tab_val (list[int]): Valeurs prises par la variable aléatoire
            moyenne (float): Espérance de la variable aléatoire
            nb_lancer (int): Nombre de lancer de partie

        Returns:
            float: Variance de la variable aléatoire
        """
        variance = 0
        for val in tab_val :
            #print("Val :", val, "Moy : ", moyenne)
            variance += (val-moyenne)**2
            #print("VAL - Moy **2 : ", (val-moyenne)**2)
            #print("Val - Moy :", (val-moyenne))
            #print()
        #print("Somme ecart-type : ", ecart_type)
        variance /= nb_lancer
        #print("ecart-type : ", ecart_type)
        return variance

    @staticmethod
    def ecart_type(tab_val : list[int], moyenne : float, nb_lancer : int) -> float :
        """Calcul l'écart-type d'une variable aléatoire

        Args:
            tab_val (list[int]): Valeurs prises par la variable aléatoire
            moyenne (float): Espérance de la variable aléatoire
            nb_lancer (int): Nombre de lancer de partie

        Returns:
            float: Ecart-type de la variable aléatoire
        """
        return sqrt(Statistic.variance(tab_val, moyenne, nb_lancer))
        