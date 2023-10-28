from .domino import *
import random
from collections import deque

class JeuDomino:
    def __init__(self, max : int):
        """Constructeur de la classe jeu domino

        Args:
            max (int): Valeur max d'un domino
        """

        self.max = max
        self.pioche = deque()
        self.domino_selected = None
        self.extremite_gauche = 0
        self.extremite_droite = 0

    def nouveauJeu(self, affichage = True) -> int:
        """Prépare et lance une nouvelle partie, nettoie les données de l'ancienne partie si il y en une

        Args:
            affichage (bool, optional): Variable permettant de savoir si l'on veut réaliser l'affichage de la fonction ou si l'on veut simplement récupérer les données de la partie. Defaults to True.

        Returns:
            int: variable x et y
        """

        # Nettoyage du jeu de domino
        self.pioche.clear()
        
        # Remplissage du jeu
        for i in range(self.max):
            for j in range(i+1):
                self.pioche.append(Domino(i, j))

        '''
        # Affichage du jeu de domino
        for i in range(len(self.pioche)):
            print(self.pioche[i].gauche, self.pioche[i].droite)
        '''

        random.shuffle(self.pioche) # Mélange des cartes

        # Choix au hasard du premier domino
        self.domino_selected = self.pioche.popleft()
        self.extremite_gauche = self.domino_selected.gauche
        self.extremite_droite = self.domino_selected.droite

        x, y = self.boucleJeu(affichage)
        return x, y
        
    def boucleJeu(self, affichage : bool = True) -> int:
        """Boucle principale du jeu qui tourne jusqu'à ce que la partie soit finie

        Args:
            affichage (bool, optional): Variable permettant de savoir si il faut réaliser l'affichage ou si c'est pour de la récupération de données. Defaults to True.

        Returns:
            int: Les données du jeu (nombre de domino placé et somme de points restant dans la pioche)
        """
        game = True
        taille_pioche = 0
        tour = 0

        while (game):
            taille_pioche = len(self.pioche) # On récupère la taille de la pioche
            if (taille_pioche > 0):
                self.domino_selected = self.pioche.popleft() # On enleve un domino de la pioche
            else :
                game = False

            if (tour < taille_pioche):

                if (affichage):
                    ### Affichage du jeu
                    print(f"\nTaille pioche : {taille_pioche}\n|{self.extremite_gauche}|..|?|..|{self.extremite_droite}|")
                    print(f"\n\t\t|{self.domino_selected.gauche}|{self.domino_selected.droite}| --- Domino de la pioche : {tour+1}/{taille_pioche}")
                    print("\n----------------------------------------------------------------------")
                
                #### Test si on peut le mettre dans les extrémités
                if (self.domino_selected.gauche == self.extremite_gauche):
                    self.extremite_gauche = self.domino_selected.droite
                    tour = 0

                elif (self.domino_selected.gauche == self.extremite_droite):
                    self.extremite_droite = self.domino_selected.droite
                    tour = 0

                elif (self.domino_selected.droite == self.extremite_gauche):
                    self.extremite_gauche = self.domino_selected.gauche
                    tour = 0

                elif (self.domino_selected.droite == self.extremite_droite):
                    self.extremite_droite = self.domino_selected.gauche
                    tour = 0

                else:
                    self.pioche.append(self.domino_selected) # Le domino ne peut pas être placé, on le remet dans la pioche
                    tour+=1
            else :
                game = False
                self.pioche.append(self.domino_selected)


        ### Affichage de fin de partie  
        if (affichage) : 
            print("\n\t\t\t-------------\n\t\t\tFIN DE PARTIE\n\t\t\t-------------\n")

        ### Calcul du nombre de domino placés
        taille_pioche = len(self.pioche)
        nb_domino_place = 28-taille_pioche # = X

        ### Calcule des points restants
        somme_points_restant = 0 # = Y
        
        while True:
            try :
                domino_restant_selected = self.pioche.pop()
                somme_points_restant += domino_restant_selected.gauche
                somme_points_restant += domino_restant_selected.droite
            except IndexError :
                break

        ### Affichage statistiques fin de partie 
        if (affichage) :
            print(f"\nNombre de domino placés : {nb_domino_place}\nSomme des points restants : {somme_points_restant}\n")

        ### Valeurs retournées
        return nb_domino_place, somme_points_restant