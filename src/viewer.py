
import matplotlib.pyplot as plt

class Viewer :
    
    def loi_de_probabilite(self, loi : list[int]) -> None :
        """Génère la représentation d'une loi de probabilite d'une variable aléatoire

        Args:
            loi (list[int]): Loi de probabilite
        """
        pas = (len(loi)//50)+1
        plt.figure()

        plt.title("Loi de probabilité")
        plt.bar([i for i in range(len(loi))], loi)
        plt.xticks([i for i in range(0, len(loi), pas)])

        plt.show()
    
    def fonction_de_repartition(self, repartition : list[float]) -> None :
        """Génère la représentation de la fonction de répartition

        Args:
            repartition (list[float]): Fonction de répartition à représenter
        """
        pas = (len(repartition)//50)+1
        plt.figure()

        plt.title("Fonction de répartition")
        plt.plot([i for i in range(len(repartition))], repartition)
        plt.xticks([i for i in range(0, len(repartition), pas)])

        plt.show()

    def nuage_de_point(self, tab_x : list, tab_y : list) -> None :
        """Génère un nuage de point à partir des coordonnées

        Args:
            tab_x (list): Coordonnées X des points
            tab_y (list): Coordonnées Y des points
        """
        pas = ((max(tab_x)-min(tab_x))//50)+1
        plt.figure()

        plt.title("Nuage de point")
        plt.scatter(tab_x, tab_y)
        plt.xticks([i for i in range(min(tab_x), max(tab_x)+1, pas)])

        plt.show()
