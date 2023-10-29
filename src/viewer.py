
import matplotlib.pyplot as plt

class Viewer :
    
    def loi_de_probabilite(self, loi : list[int]) -> None :
        """Génère la représentation d'une loi de probabilite d'une variable aléatoire

        Args:
            loi (list[int]): Loi de probabilite
        """
        plt.figure()

        plt.bar([i for i in range(len(loi))], loi)
        plt.xticks([i for i in range(len(loi))])

        plt.show()
    
    def fonction_de_repartition(self, repartition : list[float]) -> None :
        """Génère la représentation de la fonction de répartition

        Args:
            repartition (list[float]): Fonction de répartition à représenter
        """
        plt.figure()

        plt.plot([i for i in range(len(repartition))], repartition)
        plt.xticks([i for i in range(len(repartition))])

        plt.show()

    def nuage_de_point(self, tab_x : list, tab_y : list) -> None :
        """Génère un nuage de point à partir des coordonnées

        Args:
            tab_x (list): Coordonnées X des points
            tab_y (list): Coordonnées Y des points
        """
        plt.figure()

        plt.scatter(tab_x, tab_y)
   
        plt.xticks([i for i in range(min(tab_x), max(tab_x)+1)])

        plt.show()
