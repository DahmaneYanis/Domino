from .jeuDomino import JeuDomino
from math import sqrt
from .viewer import Viewer 

class Statistic :
    NOMBRE_DE_LANCER = 10000

    def __init__(self, jeuDomino : JeuDomino, visualisateur : Viewer):
        self.jeuDomino = jeuDomino
        self.viewer = visualisateur
        self.tab_val_x = [] # Tableau des nb_domino_place
        self.tab_val_y = [] # Tableau des points restant
        self.lancer_jeu_domino(self.NOMBRE_DE_LANCER)

    def lancer_jeu_domino(self, nb_lancer : int) -> None :
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
    def fonction_de_repartition(loi : list[float]) -> list[float] :
        """Créer la liste représentant la fonction de répartition d'une loi de probabilite d'une variable aléatoire

        Args:
            loi (list[float]): Loi de probabilite

        Returns:
            list[float]: Fonction de répartition
        """
        repartition = loi
        for indice in range(1, len(repartition)):
            repartition[indice] = repartition[indice-1] + repartition[indice]

        return repartition
    
    @staticmethod
    def esperance(tab_val : list[int], nb_lancer : int) -> float :
        """Calcule l'esperance d'une variable aléatoire

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
        """Calcule l'écart-type d'une variable aléatoire

        Args:
            tab_val (list[int]): Valeurs prises par la variable aléatoire
            moyenne (float): Espérance de la variable aléatoire
            nb_lancer (int): Nombre de lancer de partie

        Returns:
            float: Ecart-type de la variable aléatoire
        """
        return sqrt(Statistic.variance(tab_val, moyenne, nb_lancer))
    
    def proba_succes(self) -> float: 
        """Calcule la probabilité de succés d'une partie de domino

        Returns:
            float: Probabilité de succès
        """
        succes = 0
        for nb_point_restant in self.tab_val_y :
            if nb_point_restant == 0 : succes += 1
        return succes / self.NOMBRE_DE_LANCER
    
    def median_point_restant(self) -> int:
        """Calcule la médiane des points restants

        Returns:
            int : Médiane
        """
        temp_tab_val_y = self.tab_val_y
        temp_tab_val_y.sort()
        return temp_tab_val_y[(self.NOMBRE_DE_LANCER//2)-1]

    def get_Z(self) -> list[float]:
        """Calcule Z = X x Y

        Returns:
            list[float]: La liste des valeurs
        """
        Z = []
        for i in range(self.NOMBRE_DE_LANCER):
            Z.append(self.tab_val_x[i]*self.tab_val_y[i])

        return Z
    
    def get_X(self) -> list[float]: 
        """Getter du tableau des valeurs de X

        Returns:
            list[float]: tableau des valeurs de X
        """
        return self.tab_val_x
    
    def get_Y(self) -> list[float]:
        """Getter du tableau des valeurs de Y

        Returns:
            list[float]: tableau des valeurs de Y
        """
        return self.tab_val_y

    @staticmethod
    def covariance(esperance_z: float, esperance_x : float, esperance_y : float) -> float:
        """Calcule la covariance entre deux variables

        Args:
            esperance_z (float): Esperance de Z ou Z = X x Y
            esperance_x (float): Esperance de X
            esperance_y (float): Esperance de Y
        
        Returns:
            float : Covariance(X,Y)
        """
        return esperance_z - (esperance_x*esperance_y)
    
    @staticmethod
    def coefficient_de_correlation(cov_xy : float, ecart_x : int, ecart_y : int) -> float:
        """Calcule le coefficient de correlation entre deux variables aléatoires X et Y

        Args:
            cov_xy (float): Covariance(X,Y)
            ecart_x (int): Ecart-type de X
            ecart_y (int): Ecart-type de Y

        Returns:
            float: Coefficient de correlation entre X et
        """
        return cov_xy / (ecart_x*ecart_y)